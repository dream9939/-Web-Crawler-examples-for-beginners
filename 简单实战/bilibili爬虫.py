#导入模块
import requests
from moviepy.editor import *

#获取视频网址
url ="https://xy58x49x253x139xy.mcdn.bilivideo.cn:8082/v1/resource/upgcxcode/52/54/568395452/568395452_da2-1-100026.m4s?agrr=0&build=0&buvid=FE53AEA9-EA76-B942-F4F6-33CCCCE972AB56727infoc&bvc=vod&bw=685504&deadline=1785829591&dl=0&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv3&lrs=37&mcdnid=50059584&mid=3546612016089099&nbs=1&nettype=0&og=hw&oi=0x24098a1e8fb20d101884bf1919d8f11c&orderid=0%2C3&os=mcdn&platform=pc&prs=2&qn_dyeid=4d1e870d70ede2b9008be8cb6a717cb7&sign=1f6c42&traceid=trSwxuQzzLbonl_0_e_N&uipk=5&uparams=e%2Cgen%2Cos%2Cuipk%2Cdeadline%2Coi%2Cnbs%2Cog%2Cplatform%2Cmid%2Ctrid&upsig=19d195644b7fe64f742d04735136ed75"


#伪装成浏览器
headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
    "Referer":"https://www.bilibili.com/video/BV11P4y1K7Qp/?spm_id_from=333.337.search-card.all.click&vd_source=f60dfbe593b3f71363a1366b99a330ad"}

#获取视频

resp=requests.get(url,headers=headers)

open("wake视频.mp4","wb").write(resp.content)


#获取音频

url ="https://xy39x184x180x154xy.mcdn.bilivideo.cn:8082/v1/resource/upgcxcode/52/54/568395452/568395452_da2-1-30280.m4s?agrr=0&build=0&buvid=FE53AEA9-EA76-B942-F4F6-33CCCCE972AB56727infoc&bvc=vod&bw=124683&deadline=1785829591&dl=0&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv3&lrs=37&mcdnid=50058476&mid=3546612016089099&nbs=1&nettype=0&og=hw&oi=0x24098a1e8fb20d101884bf1919d8f11c&orderid=0%2C3&os=mcdn&platform=pc&prs=2&qn_dyeid=4d1e870d70ede2b9008be8cb6a717cb7&sign=c4752b&traceid=trHsriUEmchuvf_0_e_N&uipk=5&uparams=e%2Cos%2Cog%2Cdeadline%2Cnbs%2Cuipk%2Cgen%2Coi%2Ctrid%2Cplatform%2Cmid&upsig=aba9be644acbbbb78a842950c1c02a7c"
resp=requests.get(url,headers=headers)


open("wake音频.mp3","wb").write(resp.content)


#处理视频和音频
#导入模块



#加载视频和音频
video = VideoFileClip("视频.mp4" )
audio = AudioFileClip("音频.mp3")

#合并

final_video = video.set_audio(audio)
#保存

final_video.write_videofile("小破站视频.mp4")#, codec='libx264', audio_codec='aac', fps=video.fps, ffmpeg_params=['-vf', 'format=yuv420p'])
