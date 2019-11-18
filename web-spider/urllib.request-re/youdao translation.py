import urllib.request
import urllib.parse
import json

def youdao():
    content = input('请输入要翻译的内容：')
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15508879716913'
    data['sign'] = 'd426408cf8969ac53bf7d973e528ab09'
    data['ts'] = '1550887971691'
    data['bv'] = '617939f69fb18f112aa988d6038ae43f'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'
    data = urllib.parse.urlencode(data).encode('utf - 8')

    head = {}
    head['Referer'] = 'http://fanyi.youdao.com'
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
    req = urllib.request.Request(url, data, head)
    #上面一段伪装代码也可以用 add header() 方法实现
    #代码如下：
    #req = urllib.request.Request(url, data)
    #req.add_header('Referer', 'http://fanyi.youdao.com')
    #req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36' )

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf - 8')
    target = json.loads(html)
    print("翻译结果: %s" % (target['translateResult'][0][0]['tgt']))

if __name__ == '__main__':
    youdao()