import math
import random
from hashlib import md5
from time import time

import requests

HEADER = {}

REQUEST_URL = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
REQUEST_METHOD = 'post'
REFERER = 'http://fanyi.youdao.com/'
Cookie = {'OUTFOX_SEARCH_USER_ID': '-287583548@10.108.160.17',
          ' JSESSIONID': 'aaaHLCmqbhTPV8iqqDBix',
          ' OUTFOX_SEARCH_USER_ID_NCOO': '1332579962.4761884',
          ' UM_distinctid': '1721b76a6f8c02-0be157ff815bb4-2393f61-1fa400-1721b76a6f9a43',
          ' ___rl__test__cookies': '1589602563747'}
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
             ' Chrome/78.0.3904.108 Safari/537.36 FS'

HEADER.setdefault('User-Agent', USER_AGENT)
HEADER.setdefault('Referer', 'http://fanyi.youdao.com/')
HEADER.setdefault('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')

# 用于加密的字段：
# 加密字段破解方法：
# 1.通过搜索salt字段找到对应的js文件
# 2.找到代码：define("newweb/common/service", ["./utils", "./md5", "./jquery-1.7"], function(e, t) {
#     var n = e("./jquery-1.7");
#     e("./utils");
#     e("./md5");
#     var r = function(e) {
#         var t = n.md5(navigator.appVersion)
#           , r = "" + (new Date).getTime()
#           , i = r + parseInt(10 * Math.random(), 10);
#         return {
#             ts: r,
#             bv: t,
#             salt: i,
#             sign: n.md5("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")
#         }
#     };
# 3.从js可以看出字段数据怎么来的，参数e可以打断点来看是什么，可以看出就是要翻译的文字


app_version = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
              ' Chrome/78.0.3904.108 Safari/537.36'
t = md5(app_version.encode('utf-8')).hexdigest()
r = str(math.floor(time() * 1000))
i = r + str(random.randint(0, 9))

REQUEST_DATA = {'i': '',
                'from': 'AUTO',
                'to': 'AUTO',
                'smartresult': 'dict',
                'client': 'fanyideskweb',
                'salt': i,
                'sign': '',
                'ts': r,
                'bv': t,
                'doctype': 'json',
                'version': '2.1',
                'keyfrom': 'fanyi.web',
                'action': 'FY_BY_CLICKBUTTION'}


def make_sign(str_to_be_translated):
    sign = md5(('fanyideskweb' + str_to_be_translated + i + 'Nw(nmmbP%A-r6U3EUn]Aj').encode('utf-8')).hexdigest()
    return sign


def get_result(url, data, headers, method='post'):
    if method == 'post':
        response = requests.post(url, data=data, headers=headers, cookies=Cookie)
        return response.json()


def generate_result_dict(words: str):
    sign = make_sign(words)
    REQUEST_DATA['sign'] = sign
    REQUEST_DATA['i'] = words
    result_data = get_result(REQUEST_URL, REQUEST_DATA, HEADER, REQUEST_METHOD)
    try:
        result_list = result_data['translateResult'][0]
        for result_dict in result_list:
            yield result_dict
    except KeyError:
        yield 


def translate(words: str):
    results = generate_result_dict(words)
    final_dict = {'tgt': '', 'src': ''}
    for result in results:
        if result:
            final_dict['src'] += result['src']
            final_dict['tgt'] += result['tgt']
    return final_dict


if __name__ == '__main__':
    input_ = input('请输入需翻译的内容：')
    ret = translate(input_)
    if not ret['tgt']:
        print(f'{input_}翻译不出来！')
    else:
        print('原语言：' + ret['src'])
        print('翻译结果：' + ret['tgt'])
    
