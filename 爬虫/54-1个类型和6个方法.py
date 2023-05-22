import urllib.request
from http.client import HTTPResponse

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
assert isinstance(response, HTTPResponse)

# 一个类型和6个方法
# response是HTTPResponse类型
print(type(response))

# 以字节为单位读取
content = response.read()
print(content)

# read(5) 返回5个字节
content = response.read(5)
print(content)

# readline 读取一行
content = response.readline()

# content= response.readlines() 逐行读取


# 返回状态码
status = response.getcode()
print(status)

# 获取响应的地址
print(response.geturl())

# 获取response的请求头
print(response.getheaders())
