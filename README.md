# 项目的介绍
xxx项目接口自动化

# 环境准备
- python3.6.0
- pytest4.5.0

先安装requirements.txt
> pip install -r requirements.txt

# 执行代码
命令行输入pytest
> pytest
 
# 查看报告
./report/result.html查看测试报告

# 参数配置 pytest.ini
自己标注的内容，加注释
markers = xxx: Run xxx module cases     

命令行默认带上的参数
addopts = -s --pytest_report ./report/result.html