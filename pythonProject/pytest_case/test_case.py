# 定义byTest测试用例
import pytest
import requests

from load_data import yaml_load

msg = None

@pytest.mark.parametrize('user', yaml_load.load('.//data/user.yaml'))
def tx_01(user):
    url = 'http://localhost:8080/demo/add'
    res = requests.post(url=url, json=user)
    # res = requests.get(url)
    try:
        global msg
        msg = res.text
        print(res.text)
    except:
        pass
    assert res.text == '新增成功,name: lisi,age: 12'


def tx_02():
    print(msg)



if __name__ == '__main__':
    pytest.main(['-v','-s'])