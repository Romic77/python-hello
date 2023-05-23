# (1) 请求对象的定制
# （2）获取网页的源码
# （3）下载
import time
import urllib.request
from http.client import HTTPResponse

import lxml.etree
from lxml.etree import _Element


# 需求 下载的前十页的图片
# https://sc.chinaz.com/tupian/qinglvtupian.html   1
# https://sc.chinaz.com/tupian/qinglvtupian_page.html


def get_request(page: int):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    if page == 1:
        url = "https://sc.chinaz.com/tupian/qinglvtupian.html"
    else:
        url = "https://sc.chinaz.com/tupian/qinglvtupian_" + str(page) + ".html"

    return urllib.request.Request(url=url, headers=headers)


def get_content(request) -> str:
    handler = urllib.request.HTTPSHandler
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)
    assert isinstance(response, HTTPResponse)
    return response.read().decode('utf-8')


def down_load(content):
    tree = lxml.etree.HTML(content)
    assert isinstance(tree, _Element)
    img_name = tree.xpath("//div[@class='container']//img[@class='lazy']/@alt")
    img_src = tree.xpath("//div[@class='container']//img[@class='lazy']/@data-original")

    for i in range(len(img_name)):
        name = img_name[i]
        src = img_src[i]
        url = ('https:' + src).replace("_s", "")
        # print(name, url)
        # urlretrieve 将远程的数据下载到本地
        urllib.request.urlretrieve(url=url, filename='./images/' + name + '.jpg')


# 获取所有 //img[@class='lazy']/@src


if __name__ == '__main__':
    start_page: int = int(input("请输入开始的页码："))
    end_page: int = int(input("请输入结束的页码："))

    for page in range(start_page, end_page):
        request = get_request(page)
        content = get_content(request)
        down_load(content)
