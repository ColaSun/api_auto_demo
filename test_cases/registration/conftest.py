import pytest
import requests
import os
from common.content_sql import DbConnect


@pytest.fixture(scope="session")
def nologin_fix():
    print("不登陆前置")
    s = requests.session()
    yield s
    print("后置操作")
    s.close()


@pytest.fixture(scope="function")
def delete_user():
    '''执行sql,删除注册'''
    sql = 'delete from xxx where username = "xxx"'
    Db = DbConnect(db_cof='输入数据库ip, 账号, 密码, 端口', database='库名')
    Db.execute(sql)
    yield
    print("后置条件：数据库清理数据")


def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost", action="store",
        default="host",
        help="my option:host1 or host2")


@pytest.fixture(scope="session", autouse=True)
def host(request):
    '''设置环境变量，自动生效'''
    os.environ["host"] = request.config.getoption("--cmdhost")
    return os.environ["host"]