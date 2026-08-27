import requests

url = "https://file.moyubuluo.com/d/file/2024-12-09/4247d8f2b209cfb4b2e3569ddcd9b0b0.jpg"
headers = {"User-Agent": "Mozilla/5.0"}

resp = requests.get(url, headers=headers, timeout=20)
resp.raise_for_status()

with open("海贼王路飞壁纸.jpg","wb") as f:
    f.write(resp.content)

print("下载完成！")