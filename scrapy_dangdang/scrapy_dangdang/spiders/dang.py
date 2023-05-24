import scrapy

from scrapy_dangdang.items import ScrapyDangdangItem


class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.01.00.00.00.00.html"]

    base_url = "https://category.dangdang.com/pg"
    page = 1

    def parse(self, response):
        li_list = response.xpath("//ul[@id='component_59']/li")
        for li in li_list:
            src = li.xpath(".//img/@data-original").extract_first()
            if src:
                src = src
            else:
                src = li.xpath(".//img/@src").extract_first()
            name = li.xpath(".//img/@alt").extract_first()
            price = li.xpath(".//p[@class='price']/span[1]/text()").extract_first()
            print(name, src, price)

            dang = ScrapyDangdangItem(src=src, name=name, price=price)

            # 返回dang,通知piplines去下载
            yield dang

        if self.page <= 4:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + '-cp01.01.00.00.00.00.html'
            # 发送请求，回调parse方法
            yield scrapy.Request(url=url, callback=self.parse)
