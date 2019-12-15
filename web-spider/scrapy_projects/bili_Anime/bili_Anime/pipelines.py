# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class BiliAnimePipeline(object):
    def process_item(self, item, spider):
        sing_Anime = [item['animeName'], item['plays'], item['avg_grade'], item['gradeCounts'],
                      item['release_time'], item['tags'], item['barCounts'], item['follows'],
                      item['series'], item['membership'], item['actor_list'], item['staff_list']]

        with open('contents.csv', 'a+', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(sing_Anime)

        return item