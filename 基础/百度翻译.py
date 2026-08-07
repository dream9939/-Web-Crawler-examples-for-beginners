import requests
url="https://fanyi.baidu.com/sug"
s=input("请输入要翻译的单词：")
data={
    "kw":s
}
resp = requests.post(url,data=data)
print(resp.json())  #将服务器返回的json数据转换为字典类型并打印输出
