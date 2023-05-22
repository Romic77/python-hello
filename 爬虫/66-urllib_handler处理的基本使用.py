import urllib.request
from http.client import HTTPResponse

# 使用handler来访问百度
url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

request = urllib.request.Request(url=url, headers=headers)

# 1.获取handler对象
handler = urllib.request.HTTPHandler

# 2. 获取opener对象
opener = urllib.request.build_opener(handler)

# 3. 调用open方法
response = opener.open(request)
assert isinstance(response, HTTPResponse)
content = response.read().decode('utf-8')
print(content)
