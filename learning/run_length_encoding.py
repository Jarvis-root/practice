"""
游程编码（英语：run-length encoding，缩写RLE），又称行程长度编码或变动长度编码法，是一种与数据性质无关的无损数据压缩技术，基于“使用变动长度的码来取代连续重复出现的原始数据”来实现压缩。
举例来说，一组数据串"AAAABBBCCDEEEE"，由4个A、3个B、2个C、1个D、4个E组成，经过变动长度编码法可将数据压缩为4A3B2C1D4E（由14个单位转成10个单位）。
简言之，其优点在于将重复性高的数据量压缩成小单位；然而，其缺点在于─若该数据出现频率不高，可能导致压缩结果数据量比原始数据大，例如：原始数据"ABCDE"，压缩结果为"1A1B1C1D1E"（由5个单位转成10个单位）。
"""
def encode(input_string):
    count = 1
    prev = ""
    lst = []
    character = ''
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



if __name__ == '__main__':
    ret = encode('aaabbbbcc')
    print(ret)
    print(decode(ret))
