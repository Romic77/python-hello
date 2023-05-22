import urllib.request

url = "http://www.baidu.com"

response = urllib.request.urlopen(url)

# 获取响应的状态码
print(response.getcode())

print(response.getheaders)
# content = response.read().decode('utf-8')

# print(content)
