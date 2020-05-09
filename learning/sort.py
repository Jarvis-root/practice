"""
快速排序
递归
"""
import dis  # 反汇编模块(将计算机编码译成普通语言)
from random import randint

from numpy.random.mtrand import random_integers


def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    bigger, smaller = list(), list()
    last = sequence.pop()  # 弹出最后一个元素
    for i in sequence:
        if last < i:
            bigger.append(i)
        else:
            smaller.append(i)
    return quick_sort(smaller) + [last] + quick_sort(bigger)


def selection_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    for i in range(length-1):  # 最后一次不用遍历，因为最后一次后不会进入子循环
        least = i
        for j in range(i+1, length):
            if sequence[j] < sequence[least]:
                least = j
        sequence[i], sequence[least] = sequence[least], sequence[i]
    return sequence


a = [7, 46, 21698, 87, 132, 21, 77, 65, 4, 6, 5, 99, 0.1]
# print(a)
if __name__ == '__main__':
    # dis.dis(quick_sort)
    l = []
    for i in range(100):
        l.append(randint(10, 99999999))
    print(l)
    r = selection_sort(l)
    print(r)

