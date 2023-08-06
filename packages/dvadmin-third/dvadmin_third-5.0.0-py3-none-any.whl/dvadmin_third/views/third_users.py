import json
import mimetypes
import os
import traceback
import uuid
import urllib.parse
import hashlib
from datetime import timedelta
from wsgiref.util import FileWrapper

from pathlib import Path

import requests
from user_agents import parse
from django.conf import settings
from netifaces import interfaces, ifaddresses, AF_INET
from wechatpy import WeChatOAuth, WeChatOAuthException

from application import dispatch
from dvadmin.system.views.user import UserCreateSerializer
from dvadmin.system.models import LoginLog, Users
from dvadmin.utils.json_response import DetailResponse, ErrorResponse
from dvadmin.utils.request_util import get_request_ip, get_ip_analysis, get_browser, get_os, save_login_log
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet
from dvadmin_third.dingtalk_auth import DingTalkAuth
from dvadmin_third.feishu_auth import FeiShuAuth
from dvadmin_third.models import ThirdUsers
from rest_framework.decorators import action
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.http import StreamingHttpResponse, HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


class ThirdUsersSerializer(CustomModelSerializer):
    """
    第三方登录-序列化器
    """

    class Meta:
        model = ThirdUsers
        exclude = ['session_key']
        read_only_fields = ["id"]


class ThirdUsersViewSet(CustomModelViewSet):
    """
    第三方登录接口
    """
    queryset = ThirdUsers.objects.all()
    serializer_class = ThirdUsersSerializer


def static(request):
    path = os.path.join(Path(__file__).resolve().parent.parent, "templates", "h5", "static",
                        request.path_info.replace('/api/dvadmin_third/index/static/', ''))
    content_type, encoding = mimetypes.guess_type(path)
    resp = StreamingHttpResponse(FileWrapper(open(path, 'rb')), content_type=content_type)
    return resp


def index(request):
    return render(request, 'h5/index.html')


def check_file(request, file_name):
    txt = ''
    if file_name:
        wx_check_file_list = dispatch.get_system_config_values("third.wx_check_file")
        for ele in wx_check_file_list:
            if ele.get('key') == file_name:
                txt = ele.get('value')
                break
    return HttpResponse(txt)


def get_local_ip():
    address = [
        ifaddresses(ifacename).setdefault(AF_INET, [{'addr': '127.0.0.1'}])[0]['addr']
        for ifacename in interfaces()
    ]
    print('the IP addresses of this computer has: ', address)
    for i in address:
        if i.startswith('192.168'):
            return i
    else:
        return '127.0.0.1'
    return socket.gethostbyname(socket.gethostname())


class ThirdUsersLoginViewSet(CustomModelViewSet):
    """
    第三方登录接口
    """
    queryset = ThirdUsers.objects.all()
    serializer_class = ThirdUsersSerializer
    authentication_classes = []

    @action(methods=["GET"], detail=False, permission_classes=[])
    def scan_login_url(self, request):
        """
        获取扫码地址，一次性的，一次一个
        :param request:
        :return:
        """
        login_uid = uuid.uuid4().hex
        ip = get_request_ip(request=self.request)
        data = {
            "ip": ip,
            "browser": get_browser(request),
            "os": get_os(request)
            # "state": 1
        }
        cache.set(f"third_login_uid_{login_uid}", data, 120)
        # 0 无效，1 未扫，2 已扫，3 扫码完成,并返回token
        cache.set(f"third_login_uid_{login_uid}_state", 1, 120)
        login_type = int(self.request.query_params.get('login_type', 0))
        base_url = self.request.query_params.get('base_url', '')
        if not base_url:
            return ErrorResponse(msg="参数错误!")
        base_url = base_url.rstrip('/') if base_url.endswith('/') else base_url
        # 默认扫码登录
        url = f"api/dvadmin_third/index/#/?login_uid={login_uid}&type={login_type}&isLogin=true"
        if login_type == 1:
            # 微信公众号扫码登录
            wechat_scan_data = dispatch.get_system_config_values_to_dict('third.wechat_scan') or {}
            if not wechat_scan_data:
                return ErrorResponse(msg="微信公众号扫码登录信息未配置，请联系管理员")
            we_chat = WeChatOAuth(app_id=wechat_scan_data.get('app_id'), secret=wechat_scan_data.get('app_secret'),
                                  redirect_uri=f"{base_url}/{url}", scope='snsapi_userinfo')
            url = we_chat.authorize_url
        elif login_type == 2:
            # 飞书扫码登录
            feishu_scan_data = dispatch.get_system_config_values_to_dict('third.feishu_scan') or {}
            feishu_auth = FeiShuAuth('https://passport.feishu.cn', feishu_scan_data.get('app_id'),
                                     feishu_scan_data.get('app_secret'))
            url = feishu_auth.authorize_url(redirect_uri=f"{base_url}/{url}", )
        elif login_type == 3:
            # 钉钉扫码登录
            dingtalk_scan_data = dispatch.get_system_config_values_to_dict('third.dingtalk_scan') or {}
            dingtalk_auth = DingTalkAuth(dingtalk_scan_data.get('app_id'), dingtalk_scan_data.get('app_secret'))
            url = dingtalk_auth.authorize_url(redirect_uri=f"{base_url}/{url}", )
        return DetailResponse(data={"url": url, "login_uid": login_uid}, msg="获取成功")

    @action(methods=["GET"], detail=False, permission_classes=[])
    def get_scan_info(self, request):
        """
        获取扫码登录页面详情，可重复查询的
        :param request:
        :return:
        """
        login_uid = request.GET.get('login_uid')
        if not login_uid:
            return ErrorResponse(msg="无效二维码")
        login_data = cache.get(f"third_login_uid_{login_uid}")
        if not login_data:
            return ErrorResponse(msg="二维码已过期，请重新扫码")
        analysis_data = get_ip_analysis(login_data.get('ip'))
        cache.set(f"third_login_uid_{login_uid}_state", 2)
        return DetailResponse(data={"analysis_data": analysis_data, "login_data": login_data})

    @action(methods=["POST"], detail=False, permission_classes=[])
    def verify_whether_scan(self, request):
        """
        校验是否被扫，轮询的
        :param request:
        :return:
        """
        login_uid = self.request.data.get('login_uid')
        if not login_uid:
            return DetailResponse(data={"state": 0}, msg="无效二维码")
        login_state = cache.get(f"third_login_uid_{login_uid}_state")
        if not login_state:
            return DetailResponse(data={"state": 0}, msg="二维码已过期请重新扫码")
        # 如果 state == 3，进行登录，
        token = ''
        if login_state == 3:
            token = cache.get(f"third_login_uid_{login_uid}_token")
        return DetailResponse(data={"state": login_state, "token": token}, msg="获取成功")


class ConfirmLoginViewSet(CustomModelViewSet):
    """
    第三方登录接口-确认登录接口
    """
    queryset = ThirdUsers.objects.all()
    serializer_class = ThirdUsersSerializer

    @action(methods=["POST"], detail=False, permission_classes=[])
    def confirm_login(self, request):
        """
        扫码确认
        :param request:
        :return:
        """
        login_uid = self.request.data.get('login_uid')
        if not login_uid:
            return DetailResponse(data={"state": 0}, msg="无效二维码")
        login_state = cache.get(f"third_login_uid_{login_uid}_state")
        if not login_state:
            return DetailResponse(data={"state": 0}, msg="二维码已过期请重新扫码")
        if login_state == 3:
            return DetailResponse(data={"state": 3}, msg="二维码已扫过")
        cache.set(f"third_login_uid_{login_uid}_state", 3)
        # 进行颁发token，并记录登录日志
        ip = get_request_ip(request=request)
        analysis_data = get_ip_analysis(ip)
        analysis_data['username'] = request.user.username
        analysis_data['ip'] = ip
        analysis_data['agent'] = str(parse(request.META['HTTP_USER_AGENT']))
        analysis_data['browser'] = get_browser(request)
        analysis_data['os'] = get_os(request)
        analysis_data['creator_id'] = request.user.id
        analysis_data['dept_belong_id'] = getattr(request.user, 'dept_id', '')
        analysis_data['login_type'] = 2
        LoginLog.objects.create(**analysis_data)

        refresh = RefreshToken.for_user(self.request.user)
        cache.set(f"third_login_uid_{login_uid}_token", str(refresh.access_token), 20)
        return DetailResponse(msg="确认完成!")

    @action(methods=["POST"], detail=False, permission_classes=[])
    def third_silent_auto_login(self, request):
        """
        静默自动登录
        :param request:
        :return:
        """
        type = self.request.data.get('type')
        username = self.request.data.get('username')
        code = self.request.data.get('password')
        login_uid = self.request.data.get('login_uid')
        redirect_uri = self.request.data.get('redirect_uri')
        if not (type or username or (code and len(code) == 32)):
            return ErrorResponse('参数错误!')
        user = None
        # 如果不允许注册直接登录时，无法登录
        direct_register_login = dispatch.get_system_config_values("third.direct_register_login") or False
        if type == '0':  # 普通扫码登录
            return ErrorResponse('暂不支持该接口!')
        elif type == '1':  # 微信扫码登录
            wechat_scan_data = dispatch.get_system_config_values_to_dict('third.wechat_scan') or {}
            try:
                we_chat = WeChatOAuth(app_id=wechat_scan_data.get('app_id'), secret=wechat_scan_data.get('app_secret'),
                                      redirect_uri=f"", scope='snsapi_userinfo')
                we_chat.fetch_access_token(code=code)
                user_info = we_chat.get_user_info()
            except WeChatOAuthException as e:
                print(e)
                return ErrorResponse(msg="二维码无效，请重新扫码")
            openid = user_info.get('openid', None)
            if not openid:
                return ErrorResponse(msg="二维码无效，请重新扫码")
            third_user = ThirdUsers.objects.filter(open_id=openid, platform="wechat").first()
            if not (third_user and third_user.user):
                if not direct_register_login:
                    cache.set(f"third_login_access_token_{login_uid}", we_chat.access_token, we_chat.expires_in)
                    cache.set(f"third_login_access_token_{login_uid}_open_id", we_chat.open_id, we_chat.expires_in)
                    return ErrorResponse(code=401, msg="请使用账号密码登录后进行绑定")
                #  进行自动注册
                user, _ = Users.objects.get_or_create(
                    username=user_info.get('openid'),
                    defaults={
                        "name": user_info.get('nickname', ''),
                        "avatar": user_info.get('headimgurl'),
                        "gender": user_info.get('sex', 0),
                        "user_type": 1,
                    }
                )
                if not third_user:
                    login_ip = get_request_ip(request=request)
                    analysis = get_ip_analysis(ip=login_ip)
                    user_data = {
                        "platform": "wechat",
                        "open_id": user_info.get('openid'),
                        "union_id": user_info.get('unionid'),
                        "openname": user_info.get('nickname', ''),
                        "login_ip": login_ip,
                        "latitude": analysis.get('latitude'),
                        "longitude": analysis.get('longitude'),
                        "country": analysis.get('country'),
                        "province": analysis.get('province'),
                        "city": analysis.get('city'),
                        "district": analysis.get('district'),
                        "avatar_url": user_info.get('headimgurl'),
                        "session_key": user_info.get('session_key', None),
                    }

                    user_data["user"] = user
                    third_user = ThirdUsers.objects.create(**user_data)
                else:
                    third_user.user = user
                    third_user.save()
            user = third_user.user
        elif type == '2':  # 飞书扫码登录
            feishu_scan_data = dispatch.get_system_config_values_to_dict('third.feishu_scan') or {}
            feishu_auth = FeiShuAuth('https://passport.feishu.cn', feishu_scan_data.get('app_id'),
                                     feishu_scan_data.get('app_secret'))
            try:
                feishu_auth.authorize_user_access_token(code=code, redirect_uri=redirect_uri)
                user_info = feishu_auth.get_user_info()
            except Exception as e:
                print(e)
                return ErrorResponse(msg="二维码无效，请重新扫码")
            openid = user_info.get('open_id', None)
            if not openid:
                return ErrorResponse(msg="二维码无效，请重新扫码")
            third_user = ThirdUsers.objects.filter(open_id=openid, platform="feishu").first()
            if not (third_user and third_user.user):
                if not direct_register_login:
                    cache.set(f"third_login_access_token_{login_uid}", feishu_auth.user_access_token,
                              feishu_auth.expires_in)
                    return ErrorResponse(code=401, msg="请使用账号密码登录后进行绑定")
                #  进行自动注册
                user, _ = Users.objects.get_or_create(
                    username=openid,
                    defaults={
                        "name": user_info.get('name', '') or user_info.get('en_name', ''),
                        "avatar": user_info.get('picture'),
                        "employee_no": user_info.get('employee_no'),
                        "mobile": user_info.get('mobile', ''),
                        "email": user_info.get('email', ''),
                        "user_type": 1,
                    }
                )
                if not third_user:
                    login_ip = get_request_ip(request=request)
                    analysis = get_ip_analysis(ip=login_ip)
                    user_data = {
                        "platform": "feishu",
                        "open_id": user_info.get('open_id'),
                        "union_id": user_info.get('union_id'),
                        "openname": user_info.get('name', '') or user_info.get('en_name', ''),
                        "login_ip": login_ip,
                        "latitude": analysis.get('latitude'),
                        "longitude": analysis.get('longitude'),
                        "country": analysis.get('country'),
                        "province": analysis.get('province'),
                        "city": analysis.get('city'),
                        "district": analysis.get('district'),
                        "avatar_url": user_info.get('picture'),
                        "session_key": user_info.get('session_key', None),
                    }
                    user_data["user"] = user
                    third_user = ThirdUsers.objects.create(**user_data)
                else:
                    third_user.user = user
                    third_user.save()
            user = third_user.user
        elif type == '3':  # 钉钉扫码登录
            dingtalk_scan_data = dispatch.get_system_config_values_to_dict('third.dingtalk_scan') or {}
            dingtalk_auth = DingTalkAuth(dingtalk_scan_data.get('app_id'), dingtalk_scan_data.get('app_secret'))
            try:
                dingtalk_auth.authorize_user_access_token(code=code)
                user_info = dingtalk_auth.get_user_info()
            except Exception as e:
                print(e)
                return ErrorResponse(msg="二维码无效，请重新扫码")
            openid = user_info.get('openId', None)
            if not openid:
                return ErrorResponse(msg="二维码无效，请重新扫码")
            third_user = ThirdUsers.objects.filter(open_id=openid, platform="dingtalk").first()
            if not (third_user and third_user.user):
                if not direct_register_login:
                    cache.set(f"third_login_access_token_{login_uid}", dingtalk_auth.user_access_token,
                              dingtalk_auth.expires_in)
                    return ErrorResponse(code=401, msg="请使用账号密码登录后进行绑定")
                #  进行自动注册
                user, _ = Users.objects.get_or_create(
                    username=openid,
                    defaults={
                        "name": user_info.get('nick', ''),
                        "avatar": user_info.get('avatarUrl'),
                        "mobile": user_info.get('mobile', ''),
                        "email": user_info.get('email', ''),
                        "user_type": 1,
                    }
                )
                if not third_user:
                    login_ip = get_request_ip(request=request)
                    analysis = get_ip_analysis(ip=login_ip)
                    user_data = {
                        "platform": "dingtalk",
                        "open_id": user_info.get('openId'),
                        "union_id": user_info.get('unionId'),
                        "openname": user_info.get('nick', ''),
                        "login_ip": login_ip,
                        "latitude": analysis.get('latitude'),
                        "longitude": analysis.get('longitude'),
                        "country": analysis.get('country'),
                        "province": analysis.get('province'),
                        "city": analysis.get('city'),
                        "district": analysis.get('district'),
                        "avatar_url": user_info.get('avatarUrl'),
                        "session_key": user_info.get('session_key', None),
                    }
                    user_data["user"] = user
                    third_user = ThirdUsers.objects.create(**user_data)
                else:
                    third_user.user = user
                    third_user.save()
            user = third_user.user
        # elif type == '4':  # 短信登录
        #     pass
        else:
            return ErrorResponse(msg="登录无效，请重新扫码!")
        # 1. 根据参数校验，是否自动创建用户信息
        # 1.1 如果不创建，则返回让先用账号密码登录，在个人中心进行绑定
        # 1.2 如果创建，则需要在个人中心添加一个解除绑定功能
        # 2. 获取到用户后，签发token
        Refresh = AccessToken
        Refresh.lifetime = timedelta(days=15)
        refresh = Refresh.for_user(user)
        data = {
            "access": str(refresh),
        }
        request.user = user
        # 3. 记录登录日志
        save_login_log(request=request, login_type=int(type) + 2)
        return DetailResponse(data=data)
