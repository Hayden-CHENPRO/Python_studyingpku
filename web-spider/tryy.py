import os
import urllib.request
import http.cookiejar

os.chdir(r'C:\Users\怠惰的金枪小鱼干\Desktop')

url = 'www.baidu.com'
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = urllib.request.opener.open(url)




