import scrapy
from scrapy import Selector
from ..items import FangtianxiaItem


class WuhanNewSpider(scrapy.Spider):
    name = 'wuhan_new'
    allowed_domains = ['fang.com']
    start_urls = ['https://wuhan.newhouse.fang.com/house/s/b91/']

    def parse(self, response):
        llist = response.xpath("//div[@class='nl_con clearfix']//div[@class='nlc_img']/a")
        for ll in llist:
            house_info = ll.css('::attr(href)').get()
            house_detail_info = house_info.replace('.htm', '/housedetail.htm')
            yield scrapy.Request(house_detail_info, callback=self.parseDetail)

    def parseDetail(self, response):
        item = FangtianxiaItem()
        item['name'] = response.css('div.lpbt a.ts_linear::text').get()
        item['price'] = response.css('div.pricetd em::text').get()
        item['property_type'] = response.xpath('//ul[@class="list clearfix"]/li[1]/div[2]/text()').get()  # 物业类别
        item['building_type'] = response.css('span.bulid-type::text').get()  # 建筑类别
        # item['years_limit'] = response.css('div.pricetd em::text').get()  # 产权年限
        # item['developer'] = response.css('div.pricetd em::text').get()  # 开发商
        # item['address'] = response.css('div.pricetd em::text').get()  # 地址
        # item['loop_line'] = response.css('div.pricetd em::text').get()  # 环线位置
        item['features'] = response.xpath('//ul[@class="list clearfix"]/li[2]/div[2]/span/text()').getall()  # 项目特色
        # item['fit_type'] = response.css('div.pricetd em::text').get()  # 装修状况
        # item['sale_type'] = response.css('div.pricetd em::text').get()  # 销售状态
        # item['compelete_time'] = response.css('div.pricetd em::text').get()  # 完工时间
        # item['open_time'] = response.css('div.pricetd em::text').get()  # 开盘时间
        # item['house_area'] = response.css('div.pricetd em::text').get()  # 主力户型
        # item['land_area'] = response.css('div.pricetd em::text').get()  # 占地面积
        # item['bulid_area'] = response.css('div.pricetd em::text').get() # 建筑面积
        # item['plot_ratio'] = response.css('div.pricetd em::text').get()  # 容积率
        # item['green_ratio'] = response.css('div.pricetd em::text').get()  # 绿化率
        # item['parking_num'] = response.css('div.pricetd em::text').get()  # 停车位
        # item['bulid_num'] = response.css('div.pricetd em::text').get()  # 楼栋数
        # item['house_num'] = response.css('div.pricetd em::text').get()  # 总户数
        # item['property_fee'] = response.css('div.pricetd em::text').get()  # 物业费
        # item ['floor_info'] = response.css('div.pricetd em::text').get()  # 楼层信息
        print(item)
