# 导入Request来实现接口自动化测试
import requests

url = 'http://localhost:8080/demo/add'
# url = 'http://localhost:8080/demo/query'
data = {
    'name':'tx',
    'age': 10
}
res = requests.post(url=url,json=data)
# res = requests.get(url)
print(res.text)
