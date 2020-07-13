import requests
import pytest
import allure
import os

@allure.step("登录")
def login(s):
    url = os.environ["host"]+"/api/v1/login"
    body = {
    "username": "test",
    "password": "123456"
    }
    r = requests.post(url, json=body, verify=False)
    print(r.json())
    token = r.json()['token']
    h = {'Authorization': 'Token %s'% token}
    s.headers.update(h)
    return r.json()


@allure.step("注册")
def register(s,username="test1123", password="123456", mail="1233@qq.com"):
    '''注册'''
    url = os.environ["host"]+"/api/v1/register"
    body = {
        "username": username,
        "password": password,
        "mail": mail
    }
    r = s.post(url, json=body)
    return r



class Urse_info():
    def __init__(self, s:requests.session):
        self.s = s
    @allure.step("修改用户信息")
    def update_info(self,sex):
        url = os.environ["host"]+"/api/v1/userinfo"
        body = {"name": "test",
                "sex": sex,
                "age": 20,
                "mail": "283340479@qq.com"}
        r = self.s.post(url, json=body)
        print(r.json())
        return r.json()

    @allure.step("获取用户信息")
    def get_info(self):
        url = os.environ["host"]+"/api/v1/userinfo"
        r = self.s.get(url)
        return r.json()



if __name__ == '__main__':
    s = requests.session()
    a =Urse_info(s)
    login(s)
    b = a.get_info()
    print(b)


