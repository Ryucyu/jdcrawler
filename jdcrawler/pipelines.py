# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

client = MongoClient()
collection = client['jdcrawler']['jdphone']
a = 0

class JdcrawlerPipeline:
    def process_item(self, item, spider):
        collection.insert(dict(item))
        global a
        a = a + 1
        print(a)
        print(item)
        return item
