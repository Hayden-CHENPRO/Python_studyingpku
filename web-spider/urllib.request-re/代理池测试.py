import requests
import random
import time

ipList = [
    '122.4.51.135:9999', '183.11.235.48:9292', '163.204.245.39:9999', '182.92.194.49:8118', '114.239.252.0:9999'
]

for i in range(5):
    pxs = {'http':'http://' + random.choice(ipList)}
    print('当前使用代理：%s'%pxs)
    r = requests.get('http://icanhazip.com/', proxies=pxs)
    print(r.status_code)
    print(r.text)
    time.sleep(3)
    
