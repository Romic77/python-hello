import urllib.request
from http.client import HTTPResponse

url = 'https://weibo.cn/5546313096/info'
headers = {

    # 用户头和cookie非常重要
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Cookie": "xxx"
}

request = urllib.request.Request(headers=headers, url=url)

response = urllib.request.urlopen(request)
assert isinstance(response, HTTPResponse)
content = response.read().decode('utf-8')

with open('weibo.html', 'w', encoding='utf-8') as f:
    f.write(content)
