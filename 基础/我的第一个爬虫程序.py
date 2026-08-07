from urllib.request import urlopen
url="https://www.baidu.com/"
resp=urlopen(url)


with open("mybaidu.html","w",encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))
print("文件写入成功")