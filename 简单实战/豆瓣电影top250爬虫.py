import requests
import re
url = "http://movie.douban.com/top250"
headers = {
    "user-agent": ""
}
resp = requests.get(url, headers=headers)
page_content = resp.text  #变量page_content储存网页源码


#解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>', re.S)
#开始匹配
result = obj.finditer(page_content)

for it in result:
    print(it.group("name"))
