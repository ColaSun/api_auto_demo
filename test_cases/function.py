import requests
import allure
import os


class Info_module(object):
    '''
    个人信息模块demo
    '''
    def __init__(self, s: requests.session):
        self.s = s

    @allure.step("注册接口")
    def register(self, username="user", password="psw"):
        url = os.environ["host"] + "/api/"
        body = {
            "username": username,
            "password": password,
        }
        r = self.s.post(url, json=body)
        return r

    @allure.step("登录接口")
    def login(self, user='user', psw='psw'):
        url = os.environ["host"] + "/api"
        body = {
            "user": user,
            "psw": psw
        }
        r = requests.post(url, json=body, verify=False)
        token = r.json()['token']
        h = {'Authorization': 'Token %s' % token}
        self.s.headers.update(h)
        return r.json()

    @allure.step("修改用户信息接口")
    def update_info(self, user, phone, age):
        url = os.environ["host"]+"/api"
        body = {"name": user,
                "phone": phone,
                "age": age,
                }
        r = self.s.post(url, json=body)
        return r.json()

    @allure.step("获取用户信息接口")
    def get_info(self):
        url = os.environ["host"]+"/api"
        r = self.s.get(url)
        return r.json()


if __name__ == '__main__':
    s = requests.session()
    info = Info_module(s)


