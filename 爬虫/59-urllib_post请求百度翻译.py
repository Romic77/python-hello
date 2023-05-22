import json
import urllib.parse
import urllib.request
from http.client import HTTPResponse

url = "https://fanyi.baidu.com/sug"
data = {
    'kw': 'spider'
}

param = urllib.parse.urlencode(data).encode('utf-8')
# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

# post请求 设置请求url和请求头、请求参数
request_url = urllib.request.Request(url=url, data=param, headers=headers)

# 请求url，获取响应值
response = urllib.request.urlopen(request_url)
assert isinstance(response, HTTPResponse)

# 获取response的内容，现在返回的是string类型
content = response.read().decode('utf-8')

print(type(content))

# 将字符串转为json对象
jsonObject = json.loads(content)
print(jsonObject)
