from test_cases.function import Info_module


def test_register_01(nologin_fixtrue, delete_user):
    '''测试用例1，注册'''
    s = nologin_fixtrue
    info = Info_module(s)
    r = info.register()
    print(r.json())
    assert r.json()['msg'] == '注册成功!'


def test_register_02(nologin_fixtrue):
    '''测试用例2，重复注册'''
    s = nologin_fixtrue
    info = Info_module(s)
    r = info.register()
    r2 = info.register()
    print(r.json())
    print(r2.json())
    assert r.json()['msg'] == '注册成功!'
    assert '用户已被注册' in r2.json()['msg']

