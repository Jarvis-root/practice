
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



# dic = {'apple': 6.5,
#        'pear': 1.0,
#        'banana': 2.5,
#        'watermelon': 1.5}

# fruit = input('What fruit?')
# if fruit =='1':
#     fruit = 'apple'
# elif fruit == '2':
#     fruit = 'pear'
# elif fruit == '3':
#     fruit = 'banana'
# elif fruit == '4':
#     fruit = 'watermelon'
# price = dic[fruit]
#
# weight = float(input("{}'s weight : ".format(fruit)))
# print(weight * price)


dic = [6.5, 1.0, 2.5, 1.5]
fruit = int(input('What fruit?'))

w = float(input('weight: '))
for i, elem in enumerate(dic, start=1):

    if fruit != i:
        continue
    else:
        print(dic[i-1] * w)

import pymysql


def data_out_sql(DB, sql):
    conn = pymysql.connect(host=DB['host'], port=DB['port'], user=DB['user'], passwd=DB['password'], db=DB['dbname'],
                           charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    # 执行sql语句
    cursor.execute(sql)
    # 调出数据
    data = cursor.fetchall()
    # cols为字段信息 例如(('factory_id', 253, None, 6, 6, 0, False), ('szDeviceId', 253, None, 30, 30, 0, False),('update_time', 7, None, 19, 19, 0, False))
    cols = cursor.description
    # 执行
    conn.commit()
    conn.close()
    # 将数据truple转换为DataFrame
    col = []
    for i in cols:
        col.append(i[0])
    data = list(map(list, data))
    data = pd.DataFrame(data, columns=col)

    print(data)
    return data

