import requests
import logging
from urllib import parse
from urllib.parse import quote

# const
# open api capability
USER_ACCESS_TOKEN_URI = "/suite/passport/oauth/token"
USER_INFO_URI = "/suite/passport/oauth/userinfo"


class FeiShuAuth(object):
    def __init__(self, feishu_host, app_id, app_secret):
        self.feishu_host = feishu_host
        self.app_id = app_id
        self.app_secret = app_secret
        self._user_access_token = ""
        self._user_access_token_expires_in = 0

    @property
    def user_access_token(self):
        return self._user_access_token

    @property
    def expires_in(self):
        return self._user_access_token_expires_in

    # 这里也可以拿到user_info
    # 但是考虑到服务端许多API需要user_access_token，如文档：https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-overview
    # 建议的最佳实践为先获取user_access_token，再获得user_info
    def authorize_user_access_token(self, code, redirect_uri=""):
        # 获取 user_access_token, 依托于飞书开放能力实现.
        url = self._gen_url(USER_ACCESS_TOKEN_URI)
        headers = {
            "Content-Type": "application/json"
        }
        # 临时授权码 code 位于HTTP请求的请求体
        req_body = {
            "grant_type": "authorization_code",
            "client_id": self.app_id,
            "client_secret": self.app_secret,
            "code": code,
            "redirect_uri": redirect_uri
        }
        response = requests.post(url=url, headers=headers, json=req_body)
        data = response.json()
        self._user_access_token = data.get("access_token")
        if not self._user_access_token:
            raise Exception(data.get('error_description'))
        self._user_access_token_expires_in = response.json().get("expires_in")

    def authorize_url(self, redirect_uri, state=None):
        """获取授权跳转地址

        :return: URL 地址
        """
        redirect_uri = quote(redirect_uri, safe=b"")
        url_list = [
            self.feishu_host,
            "/suite/passport/oauth/authorize?client_id=",
            self.app_id,
            "&redirect_uri=",
            redirect_uri,
            "&response_type=code",
        ]
        if state:
            url_list.extend(["&state=", state])
        url_list.append("#feishu_redirect")
        return "".join(url_list)

    def get_user_info(self):
        # 获取 user info, 依托于飞书开放能力实现.
        # 文档链接: https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/authen-v1/authen/user_info
        url = self._gen_url(USER_INFO_URI)
        # “user_access_token” 位于HTTP请求的请求头
        headers = {
            "Authorization": "Bearer " + self.user_access_token,
            "Content-Type": "application/json",
        }
        response = requests.get(url=url, headers=headers)
        # 如需了解响应体字段说明与示例，请查询开放平台文档：
        # https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/authen-v1/authen/access_token
        return response.json()

    def _gen_url(self, uri):
        # 拼接飞书开放平台域名feishu_host和uri
        return "{}{}".format(self.feishu_host, uri)


class FeishuException(Exception):
    # 处理并展示飞书侧返回的错误码和错误信息
    def __init__(self, code=0, msg=None):
        self.code = code
        self.msg = msg

    def __str__(self) -> str:
        return "{}:{}".format(self.code, self.msg)

    __repr__ = __str__
