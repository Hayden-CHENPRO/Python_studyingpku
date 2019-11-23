# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BaidustockPipeline(object):   # 本可以直接使用这个类，但新建一个类,学习如何创建新的类，并通过配置文件使框架找到并使用这个类提取spider的item信息
    def process_item(self, item, spider):
        return item


class BaidustockInfoPipeline(object):
    def open_spider(self, spider):   # 指爬虫被调用时启动的方法
        self.f = open('BaiduStockInfo.txt', 'w')   # 打开爬虫时希望建立一个文件

    def close_spider(self, spider):   # 指爬虫被关闭时启用的方法
        self.f.close()   # 关闭爬虫时希望把文件也关闭

    def process_item(self, item, spider):   # 对每一个item进行处理时使用的方法，也是最主体的函数
        # 在文件中写入每个股票的信息
        try:
            line = str(dict(item)) + '\n'
            self.f.write(line)
        except:
            pass
        return item   # 如果有其他函数还想处理这个item，就返回这个item


# 那么我们怎么能够让框架找到这个自己新建的类呢？需要配置ITEM_PIPELINES选项！
# 找到settings.py，在其中寻找一个参数叫ITEM_PIPELINES，修改标黄部分，记得取消标注！
    #ITEM_PIPELINES = {
    #    'stockspider.pipelines.BaidustockInfoPipeline': 300,
    #}