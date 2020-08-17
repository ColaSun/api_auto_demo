import pytest
from test_cases.function import Info_module
import requests


@pytest.fixture(scope="session")
def login_fix():
    print("登陆前置：调用登录接口")
    s = requests.session()
    info = Info_module(s)
    info.login()
    yield s
    print("后置操作：数据清理")
    s.close()


if __name__ == '__main__':
    s = login_fix
    print(s)


