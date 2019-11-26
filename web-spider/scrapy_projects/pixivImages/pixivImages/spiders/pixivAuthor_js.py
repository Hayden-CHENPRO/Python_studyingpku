# -*- coding: utf-8 -*-
import scrapy
import re
import os
from pixivImages.items import ImgItem
# from scrapy import FormRequest
# import cookieDict


class PixivauthorSpider(scrapy.Spider):
    name = 'pixivAuthor_js'
    allowed_domains = ['pixiv.net']
    print("现在运行的是pixivAuthor_js")
    AuID = input("请输入抓取画师的ID：")
    start_urls = [AuID.join(['https://www.pixiv.net/ajax/user/', '/profile/all'])]

    folder = 'C:\\Users\\怠惰的金枪小鱼干\\Desktop\\画师ID_' + AuID
    os.mkdir(folder)
    os.chdir(folder)

    def parse(self, response):
        p = r'"(\d*?)":null'
        artworks_id_list = re.findall(p, response.text)   # ['77832699', ...]

        self.num = 0
        for works in artworks_id_list:
            self.works_url = 'https://www.pixiv.net/artworks/' + works
            self.logger.info("提取作品主页成功：%s", self.works_url)
            yield scrapy.Request(self.works_url, callback=self.parse_work, dont_filter=True)

    def parse_work(self, response):
        img_list = re.findall(r'https://i.pximg.net/img-original/.*?"', response.body.decode('utf-8'))
        # ['https://i.pximg.net/img-original/img/2019/09/29/00/04/33/77012924_p0.png"']

        header = {'Referer': self.works_url}

        for img_url in img_list:
            self.num += 1
            img_ori_url = img_url.split('"')[0]
            self.logger.info("提取作品原始地址成功：%s", img_ori_url)
            img_name = img_ori_url.split('/')[-1]
            yield scrapy.Request(
                img_ori_url, callback=self.parse_img, headers=header,
                dont_filter=True, meta={'img_name': img_name}
            )

    def parse_img(self, response):
        item = ImgItem()
        item['img_name'] = response.meta['img_name']
        item['picture'] = response.body

        self.logger.info("%d.图片文件名称为%s" %(self.num, item['img_name']))
        self.logger.info("headers：%s", str(response.request.headers))

        yield item

# cd code\web-spider\scrapy_projects\pixivImages
# scrapy crawl pixivAuthor_js
# 17548864