# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Created by Hayden at 2019/11/15

import urllib.request
import re


def getIpList():
    '''
    返回一个代理IP列表，列表中元素的格式如 36.7.69.56:8060
    '''

    url = 'https://www.kuaidaili.com/free/inha/1/'
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14')

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    p_ip_list = r'((?:(?:[01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}(?:[01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5]))</td>\s*<td.*\d+?</td>'
    p_ip_port = r'(?:(?:[01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}(?:[01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])</td>\s*(<td.*\d+?)</td>'

    ip_addrs_list = re.findall(p_ip_list, html)
    port_list = re.findall(p_ip_port, html)

    ipList = []

    for i in range(len(set(ip_addrs_list))):
        ip_with_port = ':'.join([ip_addrs_list[i], port_list[i].split(sep='>')[1]])
        ipList.append(ip_with_port)

    return ipList
    # 该网站一页显示15个ip，所以列表里面也是15个ip


if __name__ == '__main__':
    '''
    如果程序被单独执行时,将ip列表打印
    如果作为模块被导入其他程序，则不打印ip列表
    '''
    ipList = getIpList()

    for each in ipList:
        print(each)


