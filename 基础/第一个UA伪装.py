import requests
url="https://www.sogou.com/web?query=周杰伦"

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0"
}
resp=requests.get(url, headers=headers)
print(resp.text)