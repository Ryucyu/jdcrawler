# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    phone_name = scrapy.Field()
    price = scrapy.Field()
    pic = scrapy.Field()
    inner_href = scrapy.Field()
    name = scrapy.Field()
    RAM = scrapy.Field()
    After_taken_pixel = scrapy.Field()
    resolution = scrapy.Field()
    ROM = scrapy.Field()
    CPU = scrapy.Field()
    S5G = scrapy.Field()

