import os
import pytest
# 控制整个项目的 钩子函数, pytest的钩子函数相当于留给你一些可以开发的入口，可以新增功能


# （这一段是指从命令行传入的时候能够接收过来,实际上等于加到整个项目的配置上了）
# 添加pytest命令行参数     parser是内置fixture       # default="xxx" 不传就自动调用默认值
def pytest_addoption(parser):
    parser.addoption("--base-url",
                     action="store",
                     default="http://49.235.92.12:6009",
                     help="base-url option: url地址"
                     )


# （接收过来之后，我们要让它在整个项目生效，autouse=True是指不需要引用也能自动生效）
@pytest.fixture(scope="session", autouse=True)
def base_url_fixture(request):
    '''获取命令行参数'''
    print("当前用例运行测试环境为：{}".format(request.config.getoption("--base-url")))
    # 内置fixture,request获取配置，再获取option的变量值'--base-url'
    os.environ["base_url"] = request.config.getoption("--base-url")
    # == os.environ['base_url'] = 'http://49.235.92.12:6009'
