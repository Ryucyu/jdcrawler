# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
import time
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class seleniumMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    def process_request(self, request, spider):
        url = request.url
        spider.chrome.get(url)
        html = spider.chrome.page_source

        return HtmlResponse(url=url, body=html, request=request, encoding='utf-8')