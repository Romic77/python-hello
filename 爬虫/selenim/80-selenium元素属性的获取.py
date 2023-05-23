from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

path = './chromedriver.exe'
browser: WebDriver = webdriver.Chrome(path)
browser.get("https://www.baidu.com")

# 获取元素
input = browser.find_element(by=By.ID, value='su')

# 获取input的class属性
class_attr = input.get_attribute('class')
print(class_attr)

# 标签名称
print(input.tag_name)

# 获取元素文本
a = browser.find_element(by=By.LINK_TEXT, value="新闻")
print(a)
