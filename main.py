import requests
import json

##############################################################################################

init_url = r"https://px-conf.perimeterx.net/api/v1/mobile"
auth_type = r"https://developer.api.walmart.com/api-proxy/service/lmde/app/v4/services/auth/type"
api_login = r"https://developer.api.walmart.com/api-proxy/service/lmde/app/v4/services/auth/login"

login_payload = \
    {
        "payload": {
            "password": "Gm14605954.",
            "loginId": "gustavomogollonr@gmail.com",
            "validity": 1800
        }
    }

auth_payload = \
    {
        "payload": {
            "driverUserId": "gustavomogollonr@gmail.com"
        }
    }

init_payload = \
    {
        "app_id": "PXaY6hlFmo",
        "device_os_name": "Android",
        "device_os_version": "22",
        "sdk_version": "v1.13.1",
        "app_version": "2.22.1"
    }

##############################################################################################

init_request = requests.post(init_url, data=init_payload)
auth_request = requests.post(auth_type, data=auth_payload)
# login_request = requests.post(api_login, data=login_payload)
#
print(init_request.json())
print(auth_request)
print(auth_request.text)
# print(login_request)
