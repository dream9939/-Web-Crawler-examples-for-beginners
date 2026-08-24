import requests
url="https://www.sogou.com/web?query=周杰伦"

headers={
    "User-Agent": ""
}
resp=requests.get(url, headers=headers)
print(resp.text)
