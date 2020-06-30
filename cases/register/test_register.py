import pytest
from cases.common_function import register





def test_register_01(unlogin_fixtrue,delete_user):
    '''测试用例，注册'''
    s = unlogin_fixtrue
    r = register(s)
    print(r.json())
    assert r.json()['msg'] == '注册成功!'


def test_register_02(unlogin_fixtrue):
    '''测试用例2，重复注册'''
    s = unlogin_fixtrue
    r = register(s)
    r2 = register(s)
    print(r.json())
    print(r2.json())
    assert r.json()['msg'] == '注册成功!'
    assert '用户已被注册' in r2.json()['msg']

