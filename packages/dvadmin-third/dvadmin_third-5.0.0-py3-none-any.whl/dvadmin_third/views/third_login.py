from datetime import datetime, timedelta

from captcha.views import CaptchaStore
from django.core.cache import cache
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from wechatpy import WeChatOAuth, WeChatOAuthException

from application import dispatch
from dvadmin.system.models import Users
from dvadmin.utils.request_util import save_login_log, get_request_ip, get_ip_analysis
from dvadmin.utils.validator import CustomValidationError
from dvadmin_third.dingtalk_auth import DingTalkAuth
from dvadmin_third.feishu_auth import FeiShuAuth
from dvadmin_third.models import ThirdUsers


def bind_third_user(request, user_type, login_uid):
    """
    通过login_uid 进行绑定
    :param request:
    :param user_type:
    :param login_uid:
    :return:
    """
    print(user_type, login_uid)
    if not login_uid:
        return
    platform_dict = {
        "1": "wechat",
        "2": "feishu",
        "3": "dingtalk",
    }
    access_token = cache.get(f"third_login_access_token_{login_uid}")
    if not access_token:
        raise CustomValidationError("二维码失效，请重新扫码登录")
    if user_type == '1':  # 微信扫码登录
        wechat_scan_data = dispatch.get_system_config_values_to_dict('third.wechat_scan') or {}
        try:
            we_chat = WeChatOAuth(app_id=wechat_scan_data.get('app_id'), secret=wechat_scan_data.get('app_secret'),
                                  redirect_uri=f"", scope='snsapi_userinfo')
            open_id = cache.get(f"third_login_access_token_{login_uid}_open_id")
            user_info = we_chat.get_user_info(openid=open_id, access_token=access_token)
        except WeChatOAuthException as e:
            print(e)
            raise CustomValidationError("access_token失效，请重新登录")
        openid = user_info.get('openid', None)
        if not openid:
            raise CustomValidationError("二维码无效，请重新扫码")
        user_data = {
            "open_id": user_info.get('openid'),
            "union_id": user_info.get('unionid'),
            "openname": user_info.get('nickname', ''),
            "avatar_url": user_info.get('headimgurl'),
            "session_key": user_info.get('session_key', None),
        }
    elif user_type == '2':  # 飞书扫码登录
        feishu_scan_data = dispatch.get_system_config_values_to_dict('third.feishu_scan') or {}
        feishu_auth = FeiShuAuth('https://passport.feishu.cn', feishu_scan_data.get('app_id'),
                                 feishu_scan_data.get('app_secret'))
        feishu_auth._user_access_token = access_token
        try:
            user_info = feishu_auth.get_user_info()
        except Exception as e:
            print(e)
            raise CustomValidationError("access_token失效，请重新登录!")
        openid = user_info.get('open_id', None)
        if not openid:
            raise CustomValidationError("二维码无效，请重新扫码")
        user_data = {
            "open_id": user_info.get('open_id'),
            "union_id": user_info.get('union_id'),
            "openname": user_info.get('name', '') or user_info.get('en_name', ''),
            "avatar_url": user_info.get('picture'),
            "session_key": user_info.get('session_key', None),
        }

    elif user_type == '3':  # 钉钉扫码登录

        dingtalk_scan_data = dispatch.get_system_config_values_to_dict('third.dingtalk_scan') or {}
        dingtalk_auth = DingTalkAuth(dingtalk_scan_data.get('app_id'), dingtalk_scan_data.get('app_secret'))
        dingtalk_auth._user_access_token = access_token
        try:
            user_info = dingtalk_auth.get_user_info()
        except Exception as e:
            print(e)
            raise CustomValidationError("access_token失效，请重新登录!")
        openid = user_info.get('openId', None)
        if not openid:
            raise CustomValidationError("二维码无效，请重新扫码")
        user_data = {
            "open_id": user_info.get('openId'),
            "union_id": user_info.get('unionId'),
            "openname": user_info.get('nick', ''),
            "avatar_url": user_info.get('avatarUrl'),
            "session_key": user_info.get('session_key', None),
        }
    else:
        raise CustomValidationError("其他类型暂未支持!")

    # 进行绑定
    third_user = ThirdUsers.objects.filter(open_id=openid, platform=platform_dict[user_type]).first()
    #  进行自动注册
    if not third_user:
        login_ip = get_request_ip(request=request)
        analysis = get_ip_analysis(ip=login_ip)
        ThirdUsers.objects.create(**user_data, **{
            "platform": platform_dict[user_type],
            "login_ip": login_ip,
            "latitude": analysis.get('latitude'),
            "longitude": analysis.get('longitude'),
            "country": analysis.get('country'),
            "province": analysis.get('province'),
            "city": analysis.get('city'),
            "district": analysis.get('district'),
            "user": request.user
        })
    else:
        if third_user.user:
            raise CustomValidationError("绑定失败,已被其他账号绑定!")
        third_user.user = request.user
        third_user.save()
    return True


class ThirdLoginSerializer(TokenObtainPairSerializer):
    """
    第三方用户密码+验证码登录的序列化器:
    """
    captcha = serializers.CharField(
        max_length=6, required=False, allow_null=True, allow_blank=True
    )

    class Meta:
        model = Users
        fields = "__all__"
        read_only_fields = ["id"]

    default_error_messages = {"no_active_account": "账号/密码错误"}

    def validate(self, attrs):

        captcha = self.initial_data.get("captcha", None)
        if dispatch.get_system_config_values("base.captcha_state"):
            if captcha is None:
                raise CustomValidationError("验证码不能为空")
            self.image_code = CaptchaStore.objects.filter(
                id=self.initial_data["captchaKey"]
            ).first()
            five_minute_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if self.image_code and five_minute_ago > self.image_code.expiration:
                self.image_code and self.image_code.delete()
                raise CustomValidationError("验证码过期")
            else:
                if self.image_code and (
                        self.image_code.response == captcha
                        or self.image_code.challenge == captcha
                ):
                    self.image_code and self.image_code.delete()
                else:
                    self.image_code and self.image_code.delete()
                    raise CustomValidationError("图片验证码错误")
        data = super().validate(attrs)
        data["name"] = self.user.name
        data["userId"] = self.user.id
        data["avatar"] = self.user.avatar
        data['user_type'] = self.user.user_type
        dept = getattr(self.user, 'dept', None)
        if dept:
            data['dept_info'] = {
                'dept_id': dept.id,
                'dept_name': dept.name,
            }
        role = getattr(self.user, 'role', None)
        if role:
            data['role_info'] = role.values('id', 'name', 'key')
        request = self.context.get("request")
        request.user = self.user
        # 记录登录日志
        save_login_log(request=request)
        # 绑定账号
        bind_third_user(request, self.initial_data.get('type'), self.initial_data.get('login_uid'), )
        return {"code": 2000, "msg": "请求成功", "data": data}


class ThirdLoginView(TokenObtainPairView):
    """
    登录接口
    """
    serializer_class = ThirdLoginSerializer
    permission_classes = []
