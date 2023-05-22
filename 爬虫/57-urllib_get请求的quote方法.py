import urllib.parse
import urllib.request
from http.client import HTTPResponse

url = "http://www.baidu.com/s?wd="
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

# 将中文=周杰伦 进行Unicode编码，但是这个很麻烦，针对每个词都进行parse。 更好的方式使用encode方式
name = urllib.parse.quote('周杰伦')

# 给request添加请求头对象
urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(url + name)

assert isinstance(response, HTTPResponse)

content = response.read().decode("UTF-8")
print(content)
