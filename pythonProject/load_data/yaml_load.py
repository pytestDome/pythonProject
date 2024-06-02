import yaml

# yaml格式的数据读取
def load(path):
    file = open(path,'r',encoding='utf_8')
    data = yaml.load(file,Loader=yaml.FullLoader)
    return data