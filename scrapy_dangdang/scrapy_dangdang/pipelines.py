# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 这个管道用来生成json文件
class ScrapyDangdangPipeline:
    # 爬虫开始之前执行
    def open_spider(self, spider):
        self.fp = open('./books/book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    # 爬虫处理之后运行
    def close_spider(self, spider):
        self.fp.close()


# 这个管道用来下载图片
class DangDangDownload:
    def process_item(self, item, spider):
        url = 'http:' + item.get('src')
        filename = './books/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)

        return item
