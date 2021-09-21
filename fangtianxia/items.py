# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FangtianxiaItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    property_type = scrapy.Field()      # 物业类别
    features = scrapy.Field()           # 项目特色
    building_type = scrapy.Field()      # 建筑类别
    fit_type = scrapy.Field()           # 装修状况
    years_limit = scrapy.Field()        # 产权年限
    loop_line = scrapy.Field()          # 环线位置
    developer = scrapy.Field()          # 开发商
    address = scrapy.Field()            # 地址



    sale_type = scrapy.Field()          # 销售状态
    open_time = scrapy.Field()          # 开盘时间
    compelete_time = scrapy.Field()     # 完工时间
    house_area = scrapy.Field()         # 主力户型

    land_area = scrapy.Field()          # 占地面积
    bulid_area = scrapy.Field()         # 建筑面积
    plot_ratio = scrapy.Field()         # 容积率
    green_ratio = scrapy.Field()        # 绿化率
    parking_num = scrapy.Field()        # 停车位
    bulid_num = scrapy.Field()          # 楼栋数
    house_num = scrapy.Field()          # 总户数
    property_fee = scrapy.Field()       # 物业费
    property_fac = scrapy.Field()       # 物业公司
    floor_info = scrapy.Field()         # 楼层信息
