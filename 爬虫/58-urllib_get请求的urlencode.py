import urllib.parse
import urllib.request
from http.client import HTTPResponse

# url = "http://www.baidu.com/s?wd=周杰伦&sex=男"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
# }
#
# data = {
#     "name": "周记录",
#     "sex": "男"
# }
# # 将中文=周杰伦 进行Unicode编码，但是这个很麻烦，针对每个词都进行parse。 更好的方式使用encode方式
# encode_data = urllib.parse.urlencode(data)
# print(encode_data)


base_url = "http://www.baidu.com/s?wd="
data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}

param = urllib.parse.urlencode(data)
url = base_url + param

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

# 设置请求url和请求头
request_url = urllib.request.Request(url=url, headers=headers)

# 请求url，获取响应值
response = urllib.request.urlopen(request_url)
assert isinstance(response, HTTPResponse)

# 获取response的内容
content = response.read().decode('utf-8')
print(content)
