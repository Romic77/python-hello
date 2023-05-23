# 通过登陆 进入到主页面

import requests
import lxml.etree
from lxml.etree import _Element

url = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
params = {
    "email": "280385556@qq.com",
    "pwd": "123456",
    "code": None,
    "view_state": None,
    "view_state_generator": None,
    "denglu": "登录"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}

response = requests.get(url=url, headers=headers)
content = response.text
# 获取__VIEWSTATE 和 __VIEWSTATEGENERATOR

tree: _Element = lxml.etree.HTML(content)
view_state = tree.xpath('//*[@id="__VIEWSTATE"]/@value')
view_state_generator = tree.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')

# 获取验证码图片
code = tree.xpath('//*[@id="imgCode"]/@src')
code_url = 'https://so.gushiwen.cn' + code[0]
print(code_url)

session = requests.session()
response_code = session.get(code_url)
content_code = response_code.content
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)

params["view_state"] = view_state
params["view_state_generator"] = view_state_generator
params["code"] = input("请输入验证码:")

response_post = session.post(url=url, data=params, headers=headers)
content_post = response_post.content

with open('gushiwen.html', 'wb') as fp:
    fp.write(content_post)

# 后面使用ocr识别code
