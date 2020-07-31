from cases.common_function import login, Urse_info
import requests
import allure



@allure.story("修改个人信息，查看是否修改成功")
def test_get_info():
    s = requests.session()
    u = Urse_info(s)
    login(s)
    a = u.update_info(sex="F")
    print(a)
    b = u.get_info()
    print(b)
    assert a['data']['sex'] == "F"
    assert b['data'][0]['sex'] == "F"
