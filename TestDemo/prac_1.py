

# def _private_1(name):
#     return 'Hello, %s' % name
#
#
# def _private_2(name):
#     return 'Hi, %s' % name
#
#
# def greeting(name):
#     if len(name) > 3:
#         return _private_1(name)
#     else:
#         return _private_2(name)
#
#
#
#
# a = input('Please input something: ')
#
# print(greeting(a))

# print("*********矩形*********")
# for i in range(1,10):
#     for j in range(1,10):
#         print("{}*{}={}" .format(i,j,i*j),end=" ")
#     print(" ")
# print("*********下三角*********")
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%2d" %(i,j,i*j),end=" ")
#     print(" ")
# print("*********上三角*********")
# for i in range(1,10):
#     for j in range(i,10):
#         print("%d*%d=%2d" %(i,j,i*j),end=" ")
#     print(" ")
#
#
# for num in range(100, 1000):
#         low = num % 10
#         mid = num // 10 % 10
#         high = num // 100
#         if num == low ** 3 + mid ** 3 + high ** 3:
#             print(num)


# def approximate_size(size, a_kilobyte_is_1024_bytes=True):
#     """
#     将byte转换为容易读的单位
#     :param size:
#     :param a_kilobyte_is_1024_bytes:
#     :return:
#     """
#     s_u_f_f_i_x_e_s = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
#                        1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB', 'zib']}
#     if size < 0:
#         raise ValueError('number must be non-negative')
#     if a_kilobyte_is_1024_bytes:
#         mutiple = 1024
#     else:
#         mutiple = 1000
#     for suffix in s_u_f_f_i_x_e_s[mutiple]:
#         size /= mutiple  # size = size / mutiple
#         if size < mutiple:
#             return '{0:.1f} {1}'.format(size, suffix)  # :.f表示size去一位小数
#
#     raise ValueError('number is too big')
#
#
# if __name__ == '__main__':
#     print(approximate_size(100000000000, True))

import json
from urllib.request import urlretrieve


# json.loads('{"hh": "1"}')
# u = 'http://www.douqq.com/qqmusic/'  # <title>QQ音乐无损接口api</title>
#
#
# datas = (('hhh', str(i), d) for i in range(10) for d in range(5))
# print(datas.__next__())
# print(datas.__next__())
# print(datas.__next__())
#
# c = '温柔 《涩女郎》电视剧插曲|《落跑吧爱情》电影插曲|《侠女闯天关》台视版电视剧片尾曲.mp3'
# if ' ' in c:
#     print(c.index(' '))
# print(c[0:2])
# # breakpoint()
# d = {1 : (2 if True else 1)}
#
# print(d)
#
# n = input('dshuru')
# if n == 'y':
#     print('sdasd')

try:
    while True:
        print('111')
except KeyboardInterrupt:
    print('222')