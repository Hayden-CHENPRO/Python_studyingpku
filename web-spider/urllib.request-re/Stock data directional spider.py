# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Created by Hayden at 2019/11/17

# 获取上交所和深交所所有股票的名称和交易信息
# 此处选取的是非js动态生成的网站
# 输出：保存到文件中

import requests
import re
import traceback
from bs4 import BeautifulSoup


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r,encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getStockList(lst, stockUrl):
    html = getHtmlText(stockUrl)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0])
        except:
            continue


def getStockInfo(lst, stockUrl, fpath):
    for stock in lst:
        url = stockUrl + stock + ".html"
        html = getHtmlText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})

            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
        except:
            traceback.print_exc()   # 用try..except捕获异常，然后traceback.print_exc()打印；知道在哪一行报的错
            continue


def main():
    stock_list_url = "http://quote.eastmony.com/stocklist.html"
    stock_info_url = "http://gupiao.baidu.com/stock/"
    output_file = r"C:\Users\怠惰的金枪小鱼干\Desktop\BaiduStockInfo.txt"
    slist =[]
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)


if __name__ == '__main__':
    main()

