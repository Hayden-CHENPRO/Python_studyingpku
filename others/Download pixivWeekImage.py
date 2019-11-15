import urllib.request
import os

def download_PixivImg(folder = 'pixivWeekImage', num = 20):
    os.mkdir('C:\\Users\\怠惰的金枪小鱼干\\Desktop\\folder')
    os.chdir('C:\\Users\\怠惰的金枪小鱼干\\Desktop\\folder')

url = 'https://www.pixiv.net/ranking.php?mode=weekly'