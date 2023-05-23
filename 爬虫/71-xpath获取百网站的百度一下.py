"""
1. 获取网页的的源码
2. 解析服务器响应的文件 etree.HTML()
3. 获取相应内容
"""
import urllib.request
from http.client import HTTPResponse

from lxml import etree
from lxml.etree import _ElementTree

url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.HTTPSHandler
opener = urllib.request.build_opener(handler)
response = opener.open(request)
assert isinstance(response, HTTPResponse)

content = response.read().decode('utf-8')
print(content)

# 解析网页源码
tree = etree.HTML(content)
print(tree)
result = tree.xpath('//input[@id="su"]/@value')
print(result)
