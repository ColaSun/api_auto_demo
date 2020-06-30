import os
import yaml



def get_yml(ymlpath ):
    '''获取yaml文件数据'''
    p = open(ymlpath,"r",encoding="utf-8")
    ymldata= p.read()
    d = yaml.load(ymldata)
    print(d)
    return d



if __name__=="__main__":
    curth = os.path.dirname(os.path.realpath(__file__))
    ymlpath = os.path.join(curth, 'update_info.yml')
    info_data = get_yml(ymlpath)
