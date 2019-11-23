# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Created by Hayden at 2019/11/23

import os, sys
import urllib.request
import re
import random
import my_getProxyIp


def mkfolder():
    folder = 'C:\\Users\\怠惰的金枪小鱼干\\Desktop\\画师ID_%s'%(authorID)
    os.mkdir(folder)
    os.chdir(folder)
    return None


def setProxyIp():
    ipList = my_getProxyIp.getIpList()
    proxyIp = random.choice(ipList)
    print("本次下载使用的代理IP为：%s"%proxyIp)
    proxy_support = urllib.request.ProxyHandler({'http': proxyIp})
    return proxy_support


def reqheader(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14')
    return req


def download_img(List):
    global imgName
    num = 0

    for each in List:
        imgNum = each[20:28]  # TODO 有bug：如果指定用户的作品id不足8位数怎么改？前面可不可以用BeautifulSoup?
        imgUrl = 'https://www.pixiv.net/artworks/' + str(imgNum)

        proxy_support = setProxyIp()

        try:
            imgOrgUrl = str(each).join(['https://i.pximg.net/img-original/img/', '.png'])
            req = reqheader(imgOrgUrl)
            req.add_header('Referer', imgUrl)
            response = urllib.request.urlopen(req, timeout=10)

            imgName = str(imgNum) + '.png'

        except urllib.error.HTTPError:
            imgOrgUrl = str(each).join(['https://i.pximg.net/img-original/img/', '.jpg'])
            req = reqheader(imgOrgUrl)
            req.add_header('Referer', imgUrl)
            response = urllib.request.urlopen(req, timeout=10)

            imgName = str(imgNum) + '.jpg'

        opener = urllib.request.build_opener(proxy_support)
        opener.addheaders = [('User-Agent', 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14')]
        opener.addheaders = [('Referer', imgUrl)]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgOrgUrl, imgName, callbackfunc)
        print('\n%s 下载完成！' % imgName)

        num += 1

    print('下载任务完成，共 %d 张！' % num)


def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum：数据块数量
    @blocksize：数据块大小
    @totalsize：总数据大小
    '''
    precent = 100.0 * blocknum * blocksize / totalsize
    if precent > 100:
        precent = 100
    sys.stdout.write('\r>>>Downloding %s: %.2f%%' % (imgName, precent))
    sys.stdout.flush()


def main():
    global authorID
    authorID = input('请输入要抓取画师的P站ID:')  # 示例画师ID:20778107
    mkfolder()

    AuUrl = 'https://www.pixiv.net/member.php?id=' + str(authorID)
    req = reqheader(AuUrl)
    response = urllib.request.urlopen(req, timeout=10)
    html = response.read().decode('utf-8')

    # 匹配作品ID
    p = r'<img src="https://i.pximg.net/[^"]*(.{28}_p0)_master1200\.jpg"data-width.*?>'
    addrsList = re.findall(p, html)

    download_img(addrsList)


if __name__ == '__main__':
    main()

# TODO 设置模拟登陆