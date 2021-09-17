# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import fake_useragent
import requests
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class FangtianxiaSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class FangtianxiaDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        # ua = UserAgent(use_cache_server=False)
        location = 'C:/Users/Anooki/temp/fake_useragent_%s.json' % fake_useragent.VERSION

        ua = fake_useragent.UserAgent(path=location)
        request.headers['User-Agent'] = ua.random


class ProxyMiddleware(object):
    # def process_request(self, request, spider):
    #     # proxy = requests.get("http://www.anooki.cn:50105/get/").json().get("proxy")
    #     retry_count = 5
    #     proxy = get_proxy().get("proxy")
    #     while retry_count > 0:
    #         try:
    #             html = requests.get('http://www.baidu.com', proxies={"http": "http://{}".format(proxy)})
    #             # 使用代理访问
    #             print(proxy)
    #             request.meta['proxy'] = "http://{}".format(proxy)
    #         except Exception:
    #             retry_count -= 1
    #     # 删除代理池中代理
    #     delete_proxy(proxy)
    #     return None



    # def __init__(self, settings):
    #     # 2. 初始化中间件对象
    #     # 初始化redis
    #     self.redis = redis.Redis(host='127.0.0.1')
    #     self.redis_key = 'discovery:proxies'
    #
    #     # 所有的代理,list类型
    #     # self.proxies = settings.getlist('PROXIES')
    #     # 所有的代理的失败次数统计
    #     self.stats_redis_key = 'discovery:proxies_stats'
    #     # 所有问题的代理放到一个list中
    #     self.failed_proxy_key = 'discovery:failed_proxies'
    #     # 最大失败次数
    #     self.max_failed = 3

    # @classmethod
    # def from_crawler(cls, crawler):
    #     # 1. 判断是否打开了代理，并且创建中间件对象
    #     if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
    #         raise NotConfigured
    #     return cls(crawler.settings)

    def process_request(self, request, spider):
        # 3. 设置随机代理IP
        cur_proxy = requests.get("http://www.anooki.cn:50105/get/").json().get("proxy")
        request.meta['proxy'] = "http://{}".format(cur_proxy)
        print('use proxy: %s' % cur_proxy)

    def process_response(self, request, response, spider):
        # 4. 处理非正常的http返回码
        cur_proxy = request.meta['proxy']

        retry_count = 5
        while retry_count > 0:
            if response.status < 400:
                # 使用代理访问
                print('get http status %s when use proxy: %s' % \
                      (response.status, cur_proxy))
                return response
            else:
                retry_count -= 1
        requests.get("http://www.anooki.cn:50105/delete/?proxy={}".format(cur_proxy))
        # 记得返回response对象
        return response

    def process_exception(self, request, exception, spider):
        # 4. 处理请求过程中发和异常的情况
        # 通常是代理服务器本身挂掉了，或者网络原因
        cur_proxy = request.meta['proxy']
        print('raise exption: %s when use %s' % (exception, cur_proxy))
        # 直接从代理池中删除
        requests.get("http://www.anooki.cn:50105/delete/?proxy={}".format(cur_proxy))
        # 将IP从当前的request对象中删除
        del request.meta['proxy']
        # 从新安排该request调度下载
        return request

