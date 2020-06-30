from cases.common_function import login, Urse_info



def test_01(login_fix):
    print("用例1")
    s = login_fix
    u = Urse_info(s)
    r1 = u.update_info(sex="F")
    assert r1['data']['sex'] == "F"




def test_02(login_fix):
    print("用例1")
    s = login_fix
    u = Urse_info(s)
    print(s.headers)
    r1 = u.update_info(sex="F")
    assert r1['data']['sex'] == "F"
    r2 = u.get_info()
    assert r2['data'][0]['sex'] =="F"
