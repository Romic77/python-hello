# 1页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10


# 2页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10

import urllib.request
import urllib.parse
from http.client import HTTPResponse


def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': 10
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }

    request_data = urllib.parse.urlencode(data).encode('utf-8')
    return urllib.request.Request(url=base_url, data=request_data, headers=headers)


def get_content(request_url) -> str:
    response = urllib.request.urlopen(request_url)
    assert isinstance(response, HTTPResponse)
    return response.read().decode('utf-8')


def down_load(page: int, content: str):
    with open('kfc' + str(page) + ".json", "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == '__main__':
    start_page = int(input("请输入起始的页码"))
    end_page = int(input("请输入结束的页码"))

    for page in range(start_page, end_page + 1):
        request_url = create_request(page)
        content = get_content(request_url)
        down_load(page, content)
