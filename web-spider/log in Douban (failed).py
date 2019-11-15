# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Created by Hayden at 2019/11/15

import urllib.request, http.cookiejar

log_in_url = 'https://accounts.douban.com/passport/login'
cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

params = {
    "form_email": "18810002129",
    "form_password": "clt19980228",
    "source": "index_nav"
}

enCodeParams = urllib.parse.urlencode(params).encode('utf-8')

response = opener.open(log_in_url, enCodeParams)

if response.geturl() == 'https://www.douban.com/':
    print ('login success!')
    print(response.read().decode('utf-8'))
else:
    print('失败了...')
