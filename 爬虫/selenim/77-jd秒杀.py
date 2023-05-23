from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

path = "./chromedriver"

# 创建浏览器
browser: WebDriver = webdriver.Chrome(path)

browser.get("https://www.jd.com")
# 获取网页源码
content = browser.page_source
print(content)
