import urllib.request
from http.client import HTTPResponse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
assert isinstance(response, HTTPResponse)

content = response.read().decode('utf-8')
print(content)

with open('./douban.json', 'w', encoding='utf-8') as f:
    f.write(content)
