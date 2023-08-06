import requests
from urllib.parse import quote

USER_ACCESS_TOKEN_URI = "/v1.0/oauth2/userAccessToken"
USER_INFO_URI = "/v1.0/contact/users/me/"


class DingTalkAuth(object):
    def __init__(self, app_id, app_secret):
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

    def authorize_user_access_token(self, code):
        # 获取 user_access_token, 依托于飞书开放能力实现.
        url = "{}{}".format('https://api.dingtalk.com', USER_ACCESS_TOKEN_URI)
        headers = {
            "Content-Type": "application/json"
        }
        # 临时授权码 code 位于HTTP请求的请求体
        req_body = {
            "grantType": "authorization_code",
            "clientId": self.app_id,
            "clientSecret": self.app_secret,
            "code": code,
        }
        print("url", url, req_body)
        response = requests.post(url=url, headers=headers, json=req_body)
        print(response.json())
        data = response.json()
        self._user_access_token = data.get("accessToken")
        if not self._user_access_token:
            raise Exception(f"{data}")
        self._user_access_token_expires_in = response.json().get("expireIn")

    def authorize_url(self, redirect_uri, state=None):
        """获取授权跳转地址

        :return: URL 地址
        """
        redirect_uri = quote(redirect_uri, safe=b"")
        url_list = [
            'https://login.dingtalk.com/oauth2/auth?client_id=',
            self.app_id,
            "&redirect_uri=",
            redirect_uri,
            "&response_type=code&scope=openid&prompt=consent",
        ]
        if state:
            url_list.extend(["&state=", state])
        url_list.append("#dingtalk_redirect")
        return "".join(url_list)

    def get_user_info(self):
        url = 'https://api.dingtalk.com' + USER_INFO_URI
        headers = {
            "x-acs-dingtalk-access-token": self.user_access_token,
            "Content-Type": "application/json",
        }
        response = requests.get(url=url, headers=headers)
        return response.json()
