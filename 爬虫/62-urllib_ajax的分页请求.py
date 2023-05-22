import json
import urllib.parse
import urllib.request
from http.client import HTTPResponse


def create_request(page: int):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }

    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }

    data = urllib.parse.urlencode(data)

    return urllib.request.Request(base_url + data, headers=headers)


def get_content(request_url) -> str:
    response = urllib.request.urlopen(request_url)
    assert isinstance(response, HTTPResponse)

    return response.read().decode('utf-8')


def down_load(page: int, content: str):
    with open('douban' + str(page) + ".json", "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == '__main__':
    start_page = int(input("请输入起始的页码"))
    end_page = int(input("请输入结束的页码"))

    for page in range(start_page, end_page + 1):
        request_url = create_request(page)
        content = get_content(request_url)
        down_load(page, content)
