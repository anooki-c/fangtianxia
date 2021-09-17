import scrapy


class WuhanNewSpider(scrapy.Spider):
    name = 'wuhan_new'
    allowed_domains = ['fang.com']
    start_urls = ['https://wuhan.newhouse.fang.com/house/s/b91/']

    def parse(self, response):
        dlist = response.css('div.nlcd_name')
        print(dlist)
