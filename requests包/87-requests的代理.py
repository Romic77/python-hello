import requests

url = 'https://www.baidu.com/s?'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}

data = {
    'wd': '我的ip'
}

proxies = {
    'http': '122.243.8.26:9000'
}

response = requests.get(url=url, params=data, headers=headers, proxies=proxies)

content = response.text
with open('requests-proxy.html', 'w', encoding='utf-8') as f:
    f.write(content)
