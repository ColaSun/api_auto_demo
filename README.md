# 项目的介绍
接口自动化demo

# 环境准备
- python==3.6.8
- requests==2.22.0
- pytest==4.5.0

# 先安装requirements.txt
> pip install -r requirements.txt

# 执行代码
命令行输入pytest,运行所有用例
> pytest
 
 # 参数配置pytest.ini
 自己标注的内容，加注释 markers = info: Run info module cases
#命令行默认带上的参数 addopts = -s --alluredir ./report/allure --base-url=http://xxxx.xx:xxxx
