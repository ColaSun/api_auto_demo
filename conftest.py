import pytest
import os
import requests

#添加命令行参数
def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost", action="store",
        default="http://49.235.92.12:6009",
        help="my option:host1 or host2",
    )





@pytest.fixture(scope="session", autouse=True)
def host(request):
    '''设置环境变量，自动生效'''
    os.environ["host"] = request.config.getoption("--cmdhost")
    print(os.environ["host"])

