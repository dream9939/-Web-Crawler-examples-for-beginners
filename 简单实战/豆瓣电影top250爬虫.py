import requests
import re
url = "http://movie.douban.com/top250"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers)
page_content = resp.text  #变量page_content储存网页源码


#解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>', re.S)
#开始匹配
result = obj.finditer(page_content)

for it in result:
    print(it.group("name"))
