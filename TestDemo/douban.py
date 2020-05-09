import urllib.request as r
import ssl
import re
import requests


def login_douban(username, passwd):
    """
    使用urllib.request构建豆瓣登陆请求
    :param username: 用户
    :param passwd: 密码
    :return:
    """
    url = 'https://accounts.douban.com/j/mobile/login/basic'
    data = 'ck=&name={}&password={}&remember=false&ticket='.format(username, passwd)
    header_key = 'User-Agent'
    header_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                 '(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    request = r.Request(url)  # 创建请求对象，便于添加header
    request.add_header(header_key, header_val)  # 添加请求头
    # 避免报URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]：
    context = ssl._create_unverified_context()

    response = r.urlopen(request, data.encode('utf-8'), context=context)  # post提交的是bytes类型的数据，把字符串转化成bytes
    ret = response.read().decode('utf-8')
    if re.search('success', ret):
        print('登陆成功：', ret)


def login_douban_1(username, passwd):
    """
    使用requests构建豆瓣登陆请求
    :param username:
    :param passwd:
    :return:
    """
    url = 'https://accounts.douban.com/j/mobile/login/basic'
    # data = 'ck=&name={}&password={}&remember=false&ticket='.format(username, passwd)
    data = {
        'name': username,
        'password': passwd,
        'remember': 'false'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
               }
    reponse = requests.post(url, data=data, headers=headers)
    print(reponse.text)


def open_group():
    """
    使用requests跳转到豆瓣小组
    :return:
    """
    url = 'http://www.douban.com/group/'
    desktop_path = "C:\\Users\\Administrator\\Desktop\\"
    response = requests.get(url)
    res_str = response.content.decode('utf-8')
    # print(res_str)
    with open(desktop_path+'douban_group.html', 'w', encoding='utf-8') as f:
        f.write(res_str)
    return f


# 创建一个txt文件，文件名为mytxtfile,并向文件写入msg
def text_create(name, msg):
    desktop_path = "C:\\Users\\Administrator\\Desktop\\"  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)  # msg也就是下面的Hello world!
    file.close()


if __name__ == '__main__':
    # login_douban_1('q')
    # login_douban('qh7')
    open_group()
    # text_create('mytxtfile', 'Hello world!')
