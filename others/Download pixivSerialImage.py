import urllib.request
import os

def find_imgs(page_url):
    req = urllib.request.Request(page_url)
    req.add_header('User-Agent', 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14')
    req.add_header('Referer', page_url)

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    img_addrs_list = []

    a = html.find('a href=')
    b = html.find('.jpg', a, a + 255)
    if b != -1:
        img_addrs_list.append(html[a + 8:b + 4])

    for each in img_addrs_list:
        print(each)


def save_imgs(img_addrs):
    req = urllib.request.Request(img_addrs)
    req.add_header('User-Agent', 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14')
    req.add_header('Referer', page_url)

    img_name = str(page_num) + '.jpg'
    response = urllib.request.urlopen(req)
    pixiv_img = response.read()
    with open(img_name, 'wb') as f:
        f.write(pixiv_img)


url = 'https://www.pixiv.net/artworks/'
begin = 76783762
folder = 'C:\\Users\\怠惰的金枪小鱼干\\Desktop\\pixivSerialImage'

os.mkdir(folder)
os.chdir(folder)

page_num = begin
for i in range(num):
    page_url = url + str(page_num)
    img_addrs = find_imgs(page_url)
    save_imgs(img_addrs)
    page_num += 1