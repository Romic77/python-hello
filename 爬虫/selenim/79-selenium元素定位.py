from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

browser: WebDriver = webdriver.Chrome('./chromedriver.exe')

browser.get("https://www.baidu.com")

# 元素定位
button = browser.find_element(by=By.ID, value='su')

print(button)

# 根据xpath来获取对象
button = browser.find_element(by=By.XPATH, value='//input[@id="su"]')

print(button)

# 根据标签名字来获取对象
button = browser.find_element(by=By.TAG_NAME, value="input")
print("通过tag_name获取元素", button)

# 根据css选择器来获取对象
button = browser.find_element(by=By.CSS_SELECTOR, value="#su")
print("通过css获取元素", button)

# 获取a标签的元素，很少使用
button = browser.find_element(by=By.LINK_TEXT, value='直播')
print(button)
