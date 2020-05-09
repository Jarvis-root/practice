# enumerate() 用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个可迭代的索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1)))

# 普通FOR循环:
i = 0
seq = ['one', 'two', 'three']
for element in seq:
    print(i, seq[i])
    i += 1


# enumerate():更加简洁
for i, ele in enumerate(seq):
    print(i, ele)

"""
用“fizz”替换所有可被3整除的整数，用“buzz”替换所有可被5整除的整数，
将所有可被3和5整除的整数替换为“fizzbuzz”
"""


numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers):
    if num % 3 == 0 and num % 5 == 0:
        numbers[i] = 'fizzbuzz'
    elif num % 3 == 0:
        numbers[i] = 'fizz'
    elif num % 5 == 0:
        numbers[i] = 'buzz'

print(numbers)