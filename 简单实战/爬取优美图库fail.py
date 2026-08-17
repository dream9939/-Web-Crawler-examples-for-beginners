#导入模块
import requests
from bs4 import BeautifulSoup

#获取网页地址
url = "https://www.umtuku.com/dongwu/"

#获取网页内容
resp = requests.get(url)

#解决乱码问题
resp.encoding = "utf-8"

#打印网页内容
#print(resp.text)

#把代码交给bs4处理
main_page = BeautifulSoup(resp.text,"html.parser")

#找到div标签，class属性为fl的内容,找到其中的a标签
alist = main_page.find("div",class_="update_area_content").find_all("a")

#输出alist
#print(alist)

#遍历alist，获取每个a标签的href属性
for a in alist:
    href = a.get("href")
    #获取子页面的内容
    child_page_resp = requests.get(href)
    #设置编码格式为utf-8
    child_page_resp.encoding = "utf-8"
    #获取子页面的内容，使用.text属性获取网页内容
    child_page_text = child_page_resp.text
    #从子页面中获取图片下载路经
    child_page = BeautifulSoup(child_page_text,"html.parser")
    child_page.find("")    #这个图片网址打不开                           



