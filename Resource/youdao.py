from hashlib import md5
import math
import random
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


def translate(words: str):
    sign = make_sign(words)
    REQUEST_DATA['sign'] = sign
    REQUEST_DATA['i'] = words
    result_data = get_result(REQUEST_URL, REQUEST_DATA, HEADER, REQUEST_METHOD)
    result_dict = result_data['translateResult'][0][0]
    return result_dict


if __name__ == '__main__':
    input_ = input('请输入需翻译的内容：')
    ret = translate(input_)
    print('原语言：' + ret['src'])
    print('翻译结果：' + ret['tgt'])
