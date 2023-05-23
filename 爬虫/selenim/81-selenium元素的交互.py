import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# 定义chrome驱动地址
path = Service('./chromedriver.exe')
# 创建浏览器对象
browser: WebDriver = webdriver.Chrome(service=path)
# 打开浏览器
browser.get("https://www.baidu.com")

# 获取input文件
input = browser.find_element(by=By.ID, value='kw')

# 在文本框中输入周杰伦
input.send_keys("周杰伦")

# 获取点击按钮
button = browser.find_element(by=By.ID, value='su')
button.click()
# 如果不写等待 网页内容可能还没有响应出来，滚动条拖动不了。
time.sleep(2)

# 滑到底部，点击下一页
js = "document.documentElement.scrollTop=5000"
browser.execute_script(js)
time.sleep(2)

# 获取下一页元素
next = browser.find_element(by=By.XPATH, value='//*[@id="page"]/div/a[1]')
next.click()
time.sleep(2)

# 回到上一页
browser.back()

time.sleep(2)

# 进入下一页
browser.forward()

time.sleep(2)

# 关闭所有页面
browser.quit()
