# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest
import re


class LogintestSpider(scrapy.Spider):
    name = 'pixlog'
    allowed_domains = ['pixiv.net']
    log_url = 'https://accounts.pixiv.net/login'
    target_url = 'https://www.pixiv.net/member_illust.php?id=18302514'

    header = {'User-Agent': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14'}

    def start_requests(self):
        yield FormRequest(url=self.log_url, headers=self.header, callback=self.login,
                          dont_filter=True, meta={"cookiejar": 1})

    def login(self, response):
        p = r'<input type="hidden" name="post_key" value="(.*?)">'
        post_key = re.findall(p, response.text)[0]

        formdata = {
            'password': 'clt19980228',
            'pixiv_id': '1090552069@qq.com',
            'post_key': post_key,
            'return_to': 'https://www.pixiv.net/'
        }

        print(formdata)
        yield FormRequest(url=self.log_url, headers=self.header, formdata=formdata,
                          callback=self.after_login, dont_filter=True, meta={'cookiejar': response.meta['cookiejar']})

    def after_login(self, response):
        if '43368280' in response.text:
            print("登陆成功！")
        # elif 'reCAPTCHA' in response.text:
        #     print("出现登录验证！")
        else:
            print("登陆失败......")

        with open('pixloghtml.html', 'wb') as f:
            f.write(response.body)

# TODO 被验证码挡了唉.....
# cd code/web-spider/scrapy_projects/logintest