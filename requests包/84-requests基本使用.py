import requests

url = "https://www.baidu.com"
response = requests.get(url)
print(type(response))

# 一个类型 response的类型，6个属性

# 获取响应的文本
print(response.text)

# 设置响应格式
response.encoding = 'utf-8'

# 返回url地址
print(response.url)

# 返回文本的二进制内容
print(response.content)

# 返回状态码
print(response.status_code)

# 返回响应的请求头
print(response.headers)
