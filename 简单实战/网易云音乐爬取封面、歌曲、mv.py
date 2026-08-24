import requests

#url = "https://p1.music.126.net/02Hk2WjXmxHd1_A3biSrsg==/109951173799595653.png?imageView&quality=89"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

#resp = requests.get(url,headers=headers)

#with open("网易云音乐.jpg","wb") as f:
 #   f.write(resp.content)

#url2 = "https://m704.music.126.net/20260823214524/5fa0dd26523eca79b0b7a3c3cd3c8a8f/jdyyaac/010f/555e/0508/6e7a458911b45216563a2bdb2439d1cb.m4a?vuutv=9d/HMgUPbEmuO0glqxHzHOdMsB+CiDBqsS7D2+jWcIgEDeiOE/wSgvUDw/ss0Yl1zu5yELNXzu/x+0aAFvBg40Q6Ssm08TJ43HDUkQwU5mk=&authSecret=000001a02ec78bd50a1b0a64cdcf0006&cdntag=bWFyaz1vc193ZWIscXVhbGl0eV9leGhpZ2g"

#resp = requests.get(url2,headers=headers)

#with open("网易云音乐.m4a","wb") as f:
 #   f.write(resp.content)

url3 = "https://m704.music.126.net/20260823220704/4d2999a18b79fd3211032a5be10ee52f/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/61774054729/e308/d0d3/a289/cdc9d58a36ba589704af3f8f7cd77d0c.m4a?vuutv=fPUPAxO0/Di0Bto3Q2yip65yARpHNkYG86Y4SntLf3UgvGR8oS1WaVxrWYCR5rvZi9Helz0lXM4CQyCpjbk9rcRFHUjKnh3PEKwOaqwU/AI=&authSecret=000001a02edb60e20e640ab0f63a0007&cdntag=bWFyaz1vc193ZWIscXVhbGl0eV9leGhpZ2g"

resp = requests.get(url3,headers=headers)

with open("海贼王hope.mp4","wb") as f:
    f.write(resp.content)