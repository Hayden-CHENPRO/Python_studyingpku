# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class pixivPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        with open(item['img_name'], 'wb') as f:
            f.write(item['picture'])
        return item

    def close_spider(self,spider):
        pass