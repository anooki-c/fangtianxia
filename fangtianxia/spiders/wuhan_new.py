import scrapy
from scrapy import Selector
from ..items import FangtianxiaItem
from functools import reduce


class WuhanNewSpider(scrapy.Spider):
    name = 'wuhan_new'
    allowed_domains = ['fang.com']
    start_urls = ['https://wuhan.newhouse.fang.com/house/s/b91/']

    def parse(self, response):
        llist = response.xpath("//div[@class='nl_con clearfix']//div[@class='nlc_img']/a")
        for ll in llist:
            house_info = ll.css('::attr(href)').get()
            house_detail_info = house_info.replace('.htm', '/housedetail.htm')
            yield scrapy.Request(house_detail_info, callback=self.parseDetail, dont_filter=True)

        next_url = response.xpath('//a[@class="next"]/@href').get()
        print(next_url)
        if next_url:
            url = response.urljoin(next_url)
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parseDetail(self, response):
        item = FangtianxiaItem()
        item['name'] = response.css('div.lpbt a.ts_linear::text').get()
        item['price'] = response.css('div.pricetd em::text').get()
        item['property_type'] = response.xpath('//ul[@class="list clearfix"]/li[1]/div[2]/text()').get()  # 物业类别
        item['features'] = reduce(lambda x, y: str(x) + str(y), response.xpath(
            '//ul[@class="list clearfix"]/li[2]/div[2]/span/text()').getall())  # 项目特色
        item['building_type'] = response.css('span.bulid-type::text').get()  # 建筑类别
        item['fit_type'] = response.css(
            'div.main-item ul.list.clearfix li:nth-child(4) div:nth-child(2)::text').get().strip()  # 装修状况
        item['years_limit'] = response.css(
            'div.main-item ul.list.clearfix li:nth-child(5) div:nth-child(2) div p::text').get()  # 产权年限
        item['loop_line'] = response.css(
            'div.main-item ul.list.clearfix li:nth-child(6) div:nth-child(2)::text').get().strip()  # 环线位置
        item['developer'] = response.css(
            'div.main-item ul.list.clearfix li:nth-child(7) div:nth-child(2) a::text').get()  # 开发商
        item['address'] = response.css(
            'div.main-item ul.list.clearfix li:nth-child(8) div:nth-child(2)::text').get()  # 地址

        item['sale_type'] = response.xpath('(//ul[@class="list clearfix"])[2]/li[1]/div[2]/text()').get()  # 销售状态
        item['open_time'] = response.xpath('(//ul[@class="list clearfix"])[2]/li[2]/div[2]/text()').get()  # 开盘时间
        item['compelete_time'] = response.xpath('(//ul[@class="list clearfix"])[2]/li[3]/div[2]/text()').get()  # 交房时间
        item['house_area'] = reduce(lambda x, y: str(x) + str(y), response.xpath(
            '(//ul[@class="list clearfix"])[2]/li[6]/div[2]/a/text()').getall())  # 主力户型

        item['land_area'] = response.xpath('(//ul[@class="clearfix list"])/li[1]/div[2]/text()').get()  # 占地面积
        item['bulid_area'] = response.xpath('(//ul[@class="clearfix list"])/li[2]/div[2]/text()').get()  # 建筑面积
        item['plot_ratio'] = response.xpath('(//ul[@class="clearfix list"])/li[3]/div[2]/text()').get()  # 容积率
        item['green_ratio'] = response.xpath('(//ul[@class="clearfix list"])/li[4]/div[2]/text()').get()  # 绿化率
        item['parking_num'] = response.xpath('(//ul[@class="clearfix list"])/li[5]/div[2]/text()').get()  # 停车位
        item['bulid_num'] = response.xpath('(//ul[@class="clearfix list"])/li[6]/div[2]/text()').get()  # 楼栋数
        item['house_num'] = response.xpath('(//ul[@class="clearfix list"])/li[7]/div[2]/text()').get()  # 总户数
        item['property_fac'] = response.xpath('(//ul[@class="clearfix list"])/li[8]/div[2]/text()').get()  # 物业公司
        item['property_fee'] = response.xpath('(//ul[@class="clearfix list"])/li[9]/div[2]/text()').get()  # 物业费
        item['floor_info'] = response.xpath('(//ul[@class="clearfix list"])/li[11]/div[2]/text()').get()  # 楼层信息

        yield item
        print(item)
