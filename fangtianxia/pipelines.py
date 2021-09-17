# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import pymysql
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class FangtianxiaPipeline:
    def process_item(self, item, spider):
        # if item.get('price') == '¥44.50':
        #     return item
        # else:
        #     raise DropItem('Missing Price in {}')
        return item


# MySql数据库的存储
class MysqlPipeline:
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASS'),
            port=crawler.settings.get('MYSQL_PORT'),
            database=crawler.settings.get('MYSQL_DATABASE'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                  port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        sql = "insert into dang(title,author,pic,publish,comment,price) values('%s','%s','%s','%s','%s','%s')" % (
            item['title'], item['author'], item['pic'], item['publish'], item['comment'], item['price'])
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()
        return item


#自定义储存图片信息pipeline
class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # for image_url in item['image_urls']:
        #     yield scrapy.Request(image_url)
        yield Request(item['pic'])

    def file_path(self, request, response=None, info=None, *, item=None):
        url = request.url
        file_name = url.split("/")[-1]
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['pic'] = image_paths[0]
        return item

