"""
我也是跟着某站学习爬虫，但是教程太老，现在这个网站已经改版了
原来的xpath路径已经不适用了，所以这个这个爬虫也烂尾了，哭死
"""
#导入模块
import requests
from lxml import etree 

url = "https://beijing.zbj.com/search/service/?kw=saas&r=1"  # 目标网址

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"}

resp = requests.get(url,headers=headers)

#print(resp.text)

html = etree.HTML(resp.text)

divs = html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div')

#print("找到的元素数量：", len(divs)) 

with open('zbj_source.html', 'w', encoding='utf-8') as f:
    f.write(resp.text)

for div in divs:
    price = div.xpath("./div/div[2]/div[1]/span/text()")
    print(price)

    