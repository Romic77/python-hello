from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

browser: WebDriver = webdriver.Chrome('./chromedriver')

browser.get("https://www.baidu.com")

# 元素定位
button = browser.find_element(by=By.ID, value='su')

print(button)

button = browser.find_element(by=By.XPATH, value='//input[@id="su"]')

print(button)
