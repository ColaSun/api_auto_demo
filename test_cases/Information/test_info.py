import pytest
from test_cases.function import Info_module
from common.read_yml import get_yml
import os

cur = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
ymlpath = os.path.join(cur, 'test_data', 'update_info.yml')
info_data =get_yml(ymlpath)


@pytest.mark.parametrize("test_input,expected",
                         info_data['test_data'],
                         )
def test_01(login_fix, test_input, expected):
    print("测试用例01")
    s = login_fix
    print(s.headers)
    info = Info_module(s)
    r1 = info.update_info(sex=test_input)
    assert r1["code"] == expected["code"]
    assert r1["message"] == expected["message"]


def test_02(login_fix):
    print("测试用例02")
    s = login_fix
    info = Info_module(s)
    r1 = info.update_info(sex="F")
    assert r1['data']['sex'] == "F"


def test_03(login_fix):
    print("测试用例03")
    s = login_fix
    info = Info_module(s)
    print(s.headers)
    r1 = info.update_info(sex="F")
    assert r1['data']['sex'] == "F"
    r2 = info.get_info()
    assert r2['data'][0]['sex'] =="F"