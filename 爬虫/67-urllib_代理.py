import urllib.request
from http.client import HTTPResponse

url = "http://www.baidu.com/s?wd=ip"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
proxies = {
    'http': '58.20.184.187:9091'
}

request = urllib.request.Request(headers=headers, url=url)

# 使用ip代理
handler = urllib.request.ProxyHandler(proxies=proxies)
# handler = urllib.request.HTTPHandler
opener = urllib.request.build_opener(handler)

# 发送request
response = opener.open(request)
assert isinstance(response, HTTPResponse)
content = response.read().decode('utf-8')
print(content)

with open("proxy.html", "w", encoding="utf-8") as f:
    f.write(content)
