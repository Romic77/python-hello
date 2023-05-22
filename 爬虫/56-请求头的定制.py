import urllib.request
from http.client import HTTPResponse

url = "http://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(url)
assert isinstance(response, HTTPResponse)

content = response.read().decode("UTF-8")
print(content)
