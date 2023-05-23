import urllib.request
import urllib.error
from http.client import HTTPResponse

url = 'http://www.doudan1111.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
try:
    request = urllib.request.Request(url=url, headers=headers)
    response: HTTPResponse = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
except urllib.error.HTTPError as e:
    print("系统异常", e)
except urllib.error.URLError as u:
    print("url请求异常", u)
