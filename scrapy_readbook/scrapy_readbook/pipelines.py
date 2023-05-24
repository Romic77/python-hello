# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# useful for handling different item types with a single interface

from scrapy.utils.project import get_project_settings


class MysqlPipline:
    def open_spider(self, spider):
        settings = get_project_settings()
        self.host = settings["DB_HOST"]
        self.port = settings["DB_PORT"]
        self.user = settings["DB_USER"]
        self.password = settings["DB_PASSWORD"]
        self.name = settings["DB_NAME"]
        self.charset = settings["DB_CHARSET"]
        self.connect()

    def connect(self):
        self.conn = pymysql.Connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                    db=self.name, charset=self.charset)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "insert into book(name,src) values('{}','{}')".format(item['name'], item['src'])
        self.cursor.execute(sql)
        self.conn.commit()
        return item


class ScrapyReadbookPipeline:

    # 在爬虫文件开始的之前就执行的一个方法
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    # item就是yield后面的book对象
    def process_item(self, item, spider):
        # 以下这种模式不推荐  因为每传递过来一个对象 那么就打开一次文件  对文件的操作过于频繁

        # # (1) write方法必须要写一个字符串 而不能是其他的对象
        # # (2) w模式 会每一个对象都打开一次文件 覆盖之前的内容
        # with open('book.json','a',encoding='utf-8')as fp:
        #     fp.write(str(item))

        self.fp.write(str(item))

        return item

    # 在爬虫文件执行完之后  执行的方法
    def close_spider(self, spider):
        self.fp.close()
