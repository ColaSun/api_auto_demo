import pytest
from cases.common_function import login
import requests



@pytest.fixture(scope="session")
def login_fix():
    print("登陆前置")
    s = requests.session()
    login(s)
    if not s.headers.get('Authorization', ''):       # 未登陆成功，跳过后面的用例
        pytest.skip("未登录成功，跳过后面的用例")
    yield s
    print("后置操作")
    s.close()


@pytest.fixture(scope="session")
def bulogin_fix():
    print("不登陆前置")
    s = requests.session()
    yield s
    print("后置操作")
    s.close()


if __name__ == '__main__':
    s = login_fix
    print(s)


