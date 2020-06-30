import pytest
import requests
from common.content_sql import execute_sql



@pytest.fixture(scope="session")
def unlogin_fixtrue():
    '''不登录'''
    s = requests.session()
    return s



@pytest.fixture(scope="function")
def delete_user():
    '''执行sql,删除注册'''
    sql = 'delete from auth_user where username = "test1123"'
    execute_sql(sql)
    yield
    print("后置清理操作")
    execute_sql(sql)
