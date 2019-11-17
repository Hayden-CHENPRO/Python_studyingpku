# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Created by Hayden at 2019/11/16

import requests
import re


def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"'. html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"' ,html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(':')[1])   # 这里的eval不会出错？
            ilt.append([price,title])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = "书包"
    depth = 2
    start_url = "http://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHtmlText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


if __name__ == '__main__':
    main()
