import json
import urllib.request
from http.client import HTTPResponse
from bs4 import BeautifulSoup

url = "https://www.starbucks.com.cn/menu/"

request = urllib.request.Request(url=url)
handler = urllib.request.HTTPSHandler
opener = urllib.request.build_opener(handler)
response = opener.open(request)
assert isinstance(response, HTTPResponse)

content = response.read().decode('utf-8')

# //ul[@class='grid padded-3 product']//strong/text()

soup = BeautifulSoup(content, 'lxml')
# 获取名称
name_list = soup.select('ul[class="grid padded-3 product"] strong')
# 获取图片地址
div_src_list = soup.select('ul[class="grid padded-3 product"] div[class="preview circle"]')

base_url = "https://www.starbucks.com.cn"
for src in div_src_list:
    # print(src.attrs.get('style'))
    src = src.attrs.get('style').replace("background-image: url(\"", "").replace("\")", "")
    url = base_url + src
    print(url)
    # for name in name_list:
    #     print(name.get_text())
