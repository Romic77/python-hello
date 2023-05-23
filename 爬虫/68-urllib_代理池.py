import random
import urllib.request
from http.client import HTTPResponse

proxies_pool = [
    {
        'http': '117.68.195.56:9999'
    },
    {
        'http': '27.192.174.225:9000'
    }
]

proxies = random.choice(proxies_pool)
print(proxies)

url = "https://www.baidu.com/s?wd=ip"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

request = urllib.request.Request(url=url, headers=headers)

# 获取handler
handler = urllib.request.ProxyHandler(proxies)

opener = urllib.request.build_opener(handler)
response = opener.open(request)
assert isinstance(response, HTTPResponse)
content = response.read().decode('utf-8')

with open("proxies.html", "w", encoding="utf-8") as f:
    f.write(content)
