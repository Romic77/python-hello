from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

browser: WebDriver = webdriver.Chrome('./chromedriver.exe')

browser.get("https://www.baidu.com")
