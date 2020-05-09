"""
测试数据自动生成库hypothesis，可结合unittest和pytest使用
"""
from hypothesis import given
from hypothesis.strategies import text


# 例子1: 测试下面的游程编码函数
def encode(input_string):
    count = 1
    prev = ""
    lst = []
    # character = ''
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    entry = (character, count)
    lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q


@given(text())
def test_decode_inverts_encode(s):  # 发现bug UnboundLocalError: local variable 'character' referenced before assignment
    assert decode(encode(s)) == s
