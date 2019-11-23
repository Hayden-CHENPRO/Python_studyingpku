# -*- coding: utf-8 -*-
import scrapy
import re


class BaidustockspiderSpider(scrapy.Spider):
    name = 'BaiduStockSpider'
    allowed_domains = ['baidu.com']
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():  # 从东方财富网获取股票列表
            try:
                stock = re.findall(r'[s][hz]\d{6}', href)[0]  # 构造查询股票代码的正则表达式
                url = 'https://gupiao.baidu.com/stock/' + stock + '.html'  # 用股票代码构造访问百度股票中单支股票的链接
                yield scrapy.Request(url, callback=self.parse_stock)  # callback给出了处理这个url对应相应的处理函数parse_stock
            except:
                continue

    def parse_stock(self, response):  # 定义百度股票页面的处理函数
        infoDict = {}  # 这是要提交到item pipeline的字典类型 所以先定义一个空字典
        stockInfo = response.css('.stock-bets')  # 找到其中属性为stock-bets的区域
        name = stockInfo.css('.bets-name').extrace()[0]  # 在该区域中进一步检索bets-name，并提取字符串
        keyList = stockInfo.css('dt').extract()  # 以下提取键和值
        valueList = stockInfo.css('dd').extract()
        for i in range(len(keyList)):  # 将提取的信息保存在字典中
            key = re.findall(r'>.*</dt>', keyList(i))[0][1:-5]
            try:
                val = re.findall(r'\d+\.?.*</dd>', valueList[i])[0][0:-5]
            except:
                val = '--'
            infoDict[key] = val

        infoDict.update(  # 将股票的名称进行更新
            {'股票名称': re.findall('\s.*\(', name)[0].split()[0] + \
                     re.findall(r'\>.*\<', name)[0][1:-1]})
        yield infoDict  # 将这些信息给到item pipeline
