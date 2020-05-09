# ‐*‐ coding: utf-8 ‐*‐
# Python 3的默认编码方式为 UTF‐8 所以可以不写上面这句，python2为ASCII


# -------------转换成字典
# query = 'user=pilgrim&database=master&password=PapayaWhip'
# print(query.split('&'))  # 指定分隔符，用这个分隔符将串分离成一个字符串列表
# l = list()
# for i in query.split('&'):
#     l.append(i.split("="))
# print(l)
# dic = dict(l)
# print(dic)
# # 相当于：
# l = [['sa', 'ss'],['ww', '2']]
# d = {}
# for k, v in l:
#     print(k)
#     print(v)
#     d[k] = v
# print(d)
# -------------

print('-----------------字符串切片，分割，统计-----------------------')
string = '''string func 
python string func 
玩'''

print(string[0:6])  # 字符串本身就是字符序列，所以可以切片,但是不可以赋值因为是不可变的
print(string.splitlines())  # 将字符串按行分割，返回一个由字符串组成的列表
print(string.split())  # 指定分隔符，用这个分隔符将串分离成一个字符串列表，默认空格
print(string.rsplit())  # 从右往左
print(string.count('玩'))
string = '  ' \
         'string func '
print(string.strip())  # 删除头尾的字符，默认为所有空白字符，如空格、 制表符和换行符，也可以指定字符
print(string.rstrip())  # 删除右边的
print(string.lstrip())  # 左

print('------------------字符串变换，替换，拼接----------------------')
string = 'string func'

print(string.upper())
print(string.lower())
print(string.capitalize())  # 首字母大写
print(string.swapcase())  # 大小写字母相互转换
print(string.center(39, '*'))  # 通过在两边添加填充字符（默认为空格）让字符串居中
print(string.rjust(39, '*'))   # 在左边填充，字符串在右边
print(string.ljust(39, '*'))
print('string{} func{}'.format('0', 1))  # 字符串格式化输出
print(string.replace('string', 'Str'))  # 前面的替换为后面的，可以指定最大替换次数
print(string.join(['python ', ' study']))  # 与split相反，将string拼接到列表的字符串元素合中间，返回新的字符串


print('----------------字符串检索，查找，校验------------------------')
string = 'With a moo-moo here, 哈哈哈 and a moo-moo there'

print(string.find('a'))  # 在字符串中查找子串，找到，就返回子串的第一个字符的索引，否则返回-1
print(string.rfind('a'))  # 从右边开始找，相当于返回最大的索引
print(string.index('a'))  # 也是返回查找到子串的索引，但是没找到会引发异常
print(string.rindex('a'))
print(string.endswith('there'))
print(string.startswith('With'))
print(string.isdigit())  # 字符是否都是数字
print(string.isalpha())  # 字符是否都是字母
print(string.isspace())  # 字符是否都是空白
print(string.isalnum())  # 字符是否都是字母或数字

print(string.encode())  # 编码

