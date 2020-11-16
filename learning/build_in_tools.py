"""
从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
"""
import heapq
# import this
import json

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

"""
迭代工具 - 排列 / 组合 / 笛卡尔积
"""
import itertools

for a in itertools.permutations('ABCD', 3):  # 排列组合
    print(a)
for b in itertools.combinations('ABC', 2):
    print(b)
print(list(itertools.product('AB', '123')))  # 相当于for循环嵌套 ((x,y) for x in A for y in B)

"""
找出序列中出现次数最多的元素
"""
from collections import Counter, defaultdict

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(1))

def Filter(sTitle, sContent, sFrom, sTo, nAttachNum) :

    if (sTitle.find("交友")!=-1 and (sFrom.find("@qq.com")!=-1 or sTo.find("@kaixin.com")!=-1)) or nAttachNum>10 :
        a =1
        return True
    else :
        return False

d = defaultdict(lambda : 666)  # 自动为不存在的可以，生成value
d['a']
print(d)

#zip的使用：
attributes = ['name', 'birthday', 'gender']
values = [['jason', '2000-01-01', 'male'], ['mike', '1999-01-01', 'male'],['nancy', '2001-02-01', 'female']]
result = [dict(zip(attributes,v)) for v in values]
print(result)

# Foo("+", 2, 4)　# 返回 6
# Foo("*", 3, 5)　# 返回 15
def Foo(op, n1, n2):
    """动态语言才有的特性"""
    return eval("%d %s %d" % (n1, op, n2))


import functools

def choose(a:float ,b:float):
    if a > b:
        return a
    return b


print(choose(5, 2))
choose_other = functools.partial(choose,b=6)

print(choose_other(5))

