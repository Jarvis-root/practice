import re


def print_match_res(res):
    """打印匹配对象内容"""
    if res is not None:
        print(res.group())
    else:
        print(None)


# 两种匹配方式：
pattern = "[A-Z][a-z]+"
# 一、使用re模块函数进行匹配
res = re.match(pattern, "Tom is a good boy")  # 匹配，返回匹配对象
print(type(res))
print(res.group())

# 二、使用预编译后的正则表达式对象的方法进行匹配
obj_pattern = re.compile(pattern)  # 预编译，返回正则表达式对象
print(type(obj_pattern))
res = obj_pattern.match("Tom is a good boy")  # 匹配，返回匹配对象
print(type(res))
print(res.group())

# 匹配对象的group()和groups()方法
pattern = "\d{3}-\d{5}"
obj_pattern = re.compile(pattern)
res = obj_pattern.search("家庭电话:000-88886")
print(res.group())  # 返回整个匹配或特定子组
print(res.groups())  # 返回包含全部子组的元组

# match():从起始部分开始匹配，如果成功，返回匹配对象；失败，返回None。只匹配一次
pattern = "my"
# res=re.compile(pattern).match("my name is li")
res = re.match(pattern, "my name is li")
print_match_res(res)

# search(): 从任意位置开始匹配，如果成功，返回匹配对象；失败，返回None。只匹配一次
pattern = "my"
# res=re.compile(pattern).search("it's my dog")
res = re.search(pattern, "my name is li")
print_match_res(res)

# 查找全部
# findall(),finditer()
res = re.findall(r"th\w+", "This and that", re.I)
print(res)
res = re.finditer(r"th\w+", "This and that", re.I)
print(res)
print(next(res).group(), next(res).group())

# 替换
# sub(),subn()
res = re.sub("funny", "fool", "You are so funny")
print(res)
res = re.subn("funny", "fool", "You are so funny")
print(res)

# 分割
# splite()
res = re.split("\.", "Mr.Smith")
print(res)

print("#" * 50)
# 择一匹配符号 a|b
pattern = "I|You|She"
res = re.compile(pattern, flags=re.IGNORECASE).match("i love you")
print_match_res(res)
res = re.compile(pattern, flags=re.I).search("who love you")
print_match_res(res)

# 匹配任意单个字符 .
pattern = "w{3,}\..+\.com"
res = re.match(pattern, "wwww.google.com/index.html", re.I)
print_match_res(res)

# 字符集 [abc] [a-z0-9]
pattern = "[A-Za-z0-9_]*\."
res = re.match(pattern, "Python3.?")
print_match_res(res)

# 特殊字符 \d \w \s \b \\
# 重复 + ? * {N,} {N,M}
# 分组 (...)
pattern = "\w+@(\w{1,10}\.)*([a-z]*)"
res = re.match(pattern, "li@gmail.com")
print_match_res(res)
res = re.match(pattern, "li@qq.vip.org")
print_match_res(res)
print(res.group(0), res.group(1), res.group(2), sep="\t")
print(res.groups())

# 匹配字符串的起始和结尾，单词边界  ^a z$ \A \Z \b \B
pattern = r"^the"
# pattern=r"\Athe"
res = re.search(pattern, "The end of the world")
print_match_res(res)
res = re.search(pattern, "they smile")
print_match_res(res)

pattern = r"cry$"
# pattern=r"cry\Z"
res = re.search(pattern, "they cry")
print_match_res(res)

res = re.search(r"\bthe", "bit the dog")
print_match_res(res)
res = re.search(r"\Bhe", "bit the dog")
print_match_res(res)

