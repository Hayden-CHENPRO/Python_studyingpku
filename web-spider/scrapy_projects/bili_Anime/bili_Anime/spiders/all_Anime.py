# -*- coding: utf-8 -*-
import scrapy
import os
import re
from bili_Anime.items import BiliAnimeItem


class AllAnimeSpider(scrapy.Spider):
    name = 'all_Anime'
    allowed_domains = ['bilibili.com']
    start_urls = [str(i).join(['https://api.bilibili.com/pgc/season/index/result?season_version=1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=2&st=1&sort=0&page=',
                            '&season_type=1&pagesize=20&type=1']) for i in range(1,112)]

    folder = r'C:\Users\怠惰的金枪小鱼干\Desktop'
    os.chdir(folder)
    print('1.到这了')

    def parse(self, response):
        p = r'"media_id":(\d*?),"'
        anime_id_list = re.findall(p, response.text)
        print(anime_id_list)
        print('2.到这了')

        for each in anime_id_list:
            work_main_page = 'https://www.bilibili.com/bangumi/media/md' + each
            self.logger.info('提取番剧主页成功：%s', work_main_page)
            yield scrapy.Request(work_main_page, callback=self.parse_workPage, dont_filter=True)

    def parse_workPage(self, response):
        item = BiliAnimeItem()
        item['animeName'] = re.findall(r'<span class="media-info-title-t">(.*?)<', response.text)[0]
        item['plays'] = re.findall(r'总播放</span> <em>(.*?)<', response.text)[0]

        try:
            item['avg_grade'] = re.findall(r'class="media-info-score-content">(.*?)<', response.text)[0]
        except IndexError:
            item['avg_grade'] = ""

        try:
            item['gradeCounts'] = re.findall(r'class="media-info-review-times">(.*?)<', response.text)[0][:-2]
        except IndexError:
            item['gradeCounts'] = ""

        item['release_time'] = re.findall(r'class="media-info-time"><span>(.*?)<', response.text)[0][:-2]

        item['tags'] = re.findall(r'class="media-tag">(.*?)<', response.text)
        if item['tags'] == []:
            item['tags'] = ['']

        item['barCounts'] = re.findall(r'弹幕总数</span> <em>(.*?)<', response.text)[0]
        item['follows'] = re.findall(r'追番人数</span> <em>(.*?)<', response.text)[0]
        item['series'] = re.findall(r'开播</span> <span>(.*?)<', response.text)[0]
        item['membership'] = [0 if len(re.findall(r'class="pay-btn "', response.text))==0 else 1][0]

        pa = re.compile(r'"actors":"(.*?)"', re.S)
        item['actor_list'] = re.findall(pa, response.text)[0]

        ps = re.compile(r'"staff":"(.*?)"', re.S)
        item['staff_list'] = re.findall(ps, response.text)[0]

        yield item
