import pytest
from cases.common_function import login, Urse_info
from common.read_yml import get_yml
import os
import allure


curth = os.path.dirname(os.path.realpath(__file__))
ymlpath = os.path.join(curth, 'update_info.yml')
info_data =get_yml(ymlpath)


@pytest.mark.parametrize("test_input,expected",
                         info_data['test_info_params_data'],
                         ids= [
                             "修改个人信息sex=F",
                             "修改个人信息sex=F",

                         ]
)
@allure.title("修改用户信息")
@allure.story("修改用户的信息")
def test_01(login_fix, test_input, expected):
    print("用例")
    s = login_fix
    u = Urse_info(s)
    print(s.headers)
    r1 = u.update_info(sex=test_input)
    assert r1["code"] == expected["code"]
    assert r1["message"] == expected["message"]


@pytest.mark.skip("跳过原因：有bug")
def test_02():
    "跳过这条用例"
    print("跳过的用例")

@pytest.mark.xxx
def test_03():
    print("xxx模块用例")

