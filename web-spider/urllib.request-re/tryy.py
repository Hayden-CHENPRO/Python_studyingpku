import requests

url = 'https://pixon.ads-pixiv.net/show?zone_id=logo_side&format=js&s=2&up=0&a=21&ng=g&l=zh&uri=%2Fajax%2Fuser%2F_PARAM_%2Fprofile%2Ftop&is_spa=1&K=5e890c295bf58&ab_test_digits_first=93&Yuid=FJM4ZYQ&suid=Pg9b7rwtdinroc7nj&num=5ddc887e273&t=BU9SQkS-zU&t=EZQqoW9r8g&t=HLWLeyYOUF&t=IVwLyT8B6k&t=Ig5OcZugU6&t=K0rq4tmPAD&t=OEXgaiEbRa&t=b8b4-hqot7&t=kP7msdIeEU&t=mIFanJgKGQ&t=pvU1D1orJa&t=uG0wcfxlfN&t=y8GNntYHsi'

header = {'User-Agent': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14'}

def getHtml():
    try:
        r = requests.get(url, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
        print('sdfa!')
    except:
        return '出错'

getHtml()