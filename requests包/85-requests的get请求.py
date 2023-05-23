import requests

url = "https://www.baidu.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}

data = {
    'wd': '北京'
}

response = requests.get(url, data=data, headers=headers)
print(response.text)
