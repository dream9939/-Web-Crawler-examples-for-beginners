#导入模块
import requests

#准备好网址
url = "https://www.pearvideo.com/video_1807134"

contid = url.split("_")[1]

videostatus = f"https://www.pearvideo.com/videoStatus.jsp?contId={contid}&mrd=0.47883279279355884"

#设置请求头
headers = {
    "referer": "https://www.pearvideo.com/video_1807134",#这是防盗链
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

resp = requests.get(videostatus,headers=headers)

dic = resp.json()

srcurl = dic['videoInfo']['videos']['srcUrl']

systemtime = dic['systemTime']

srcUrl = srcurl.replace(systemtime,f'cont-{contid}')

#print(srcUrl)

#下载视频

with open('b.mp4',mode='wb')as f:

    f.write(requests.get(srcUrl).content)

    print("文件写入成功")