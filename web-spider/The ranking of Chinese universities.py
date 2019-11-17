# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Created by Hayden at 2019/11/16

import requests
import bs4
from bs4 import BeautifulSoup


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(uList, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):   # 检测tr标签的类型，如果tr不是bs4定义的tag类型则过滤掉
            tds = tr('td')   # 查询tr中的td标签
            uList.append([tds[0].string, tds[1].string, tds[2].string])


def printUnivList(uList, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"   # \t为水平制表符；{3}表示学校名称这一栏用format的第三个参数（即chr(12288)填充）
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))  # chr(12288)为中文空格，用于解决中西文长度不一致导致对不齐的问题
    for i in range(num):
        u = uList[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHtmlText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)


if __name__ == '__main__':
    main()
