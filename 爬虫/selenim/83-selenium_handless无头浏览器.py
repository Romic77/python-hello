# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.webdriver import WebDriver
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
#
# # 获取chrome的浏览器位置
# path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# chrome_options.binary_location = path
# browser: WebDriver = webdriver.Chrome(options=chrome_options)
#
# url = 'https://www.baidu.com'
# browser.get(url)
# browser.save_screenshot('baidu.png')
#
# # 关闭浏览器
# browser.quit()


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


def browser():
    options = Options()

    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    # 获取chrome的浏览器位置
    path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    options.binary_location = path
    browser: WebDriver = webdriver.Chrome(options=options)
    return browser


browser = browser()
url = 'https://www.baidu.com'
browser.get(url)
browser.save_screenshot('baidu.png')

# 关闭浏览器
browser.quit()
