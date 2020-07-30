import pytest
from cases.common_function import login, Urse_info
from common.read_yml import get_yml
import os
from setting import base_dir


ymlpath = os.path.join(base_dir, 'test_data', 'update_info.yml')
info_data =get_yml(ymlpath)


@pytest.mark.parametrize("test_input,expected",
                         info_data['test_info_params_data'],
                         ids= [
                             "修改个人信息sex=F",
                             "修改个人信息sex=F",

                         ]
)
def test_01(login_fix, test_input, expected):
    print("用例")
    s = login_fix
    print(s.headers)
    a = Urse_info(s)
    r1 =a.update_info(sex=test_input)
    assert r1["code"] == expected["code"]
    assert r1["message"] == expected["message"]


@pytest.mark.skip("跳过原因：有bug")
def test_02():
    "跳过这条用例"
    print("跳过的用例")