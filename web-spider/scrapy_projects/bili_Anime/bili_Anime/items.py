# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BiliAnimeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    animeName = scrapy.Field()       # 番剧名称
    plays = scrapy.Field()           # 播放量
    avg_grade = scrapy.Field()       # 平均评分
    gradeCounts = scrapy.Field()     # 评分人数
    release_time = scrapy.Field()    # 上映时间
    tags = scrapy.Field()            # 标签
    barCounts = scrapy.Field()       # 弹幕量
    follows = scrapy.Field()         # 追番人数
    series = scrapy.Field()          # 剧集数
    membership = scrapy.Field()      # 大会员许可
    actor_list = scrapy.Field()      # 声优表
    staff_list = scrapy.Field()      # 职员表
