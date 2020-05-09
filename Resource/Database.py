# from typing import Any

import MySQLdb
import random, time


class Database(object):

    def __init__(self, host, user, password, db, charset='utf8'):
        """

        :param host:
        :param user:
        :param password:
        :param db:
        :param charset:
        """
        try:
            self.con = MySQLdb.connect(
                host=host,
                user=user,
                password=password,
                db=db,
                charset=charset
            )
        except Exception as e:
            print(e)

    def close_connect(self):
        return self.con.close()

    def execute_sql(self, sql):

        cursor = self.con.cursor()
        cursor.execute(sql)
        return cursor

    def yield_row(self, sql):
        cursor = self.execute_sql(sql)
        for n in range(cursor.rowcount):  # rowcount: 只读属性，返回执行execute()方法后影响的行数
            row = cursor.fetchone()
            yield row

    def query_many(self, sql1, row_number=None):
        """

        :param sql1:
        :param row_number: 查询的行数，None即查询所有数据，其他数字即查询行数
        :return: [(...), (...) ...]
        """
        row_list = list()
        for index, row in enumerate(self.yield_row(sql1)):
            row_list.append(row)
            if row_number:
                if index+1 == row_number:
                    break
        return row_list

    def insert(self, dml):
        """

        :param dml: DML语句（除select外的)
        :return:
        """
        cursor = self.execute_sql(dml)
        self.con.commit()
        return cursor.rowcount

    def insert_many(self, sql2, list_of_list):

        # "
        return self.con.cursor().executemany(sql2, list_of_list)


if __name__ == '__main__':
    s = "SELECT * FROM `account`;"
    a = Database('192.168.1.4', 'root', '123456', 'test')

    #  使用cursor.execute插入，比executemany慢很多
    # t3 = time.time()
    # i = 0
    # for id in range(9999, 99999):
    #     name = random.choice(['王上', '赵小康', '李小强', 'Shaw', 'Mark', 'shabi', 'Python'])
    #     sex = random.choice(['男', '女'])
    #     money = random.uniform(1, 1000)
    #     account = random.randint(123456789, 999999999)
    #     dml = f"INSERT INTO `account`(`id`, `Name`, `Sex`, `Money`, `Account`) VALUES ({id}, '{name}', '{sex}', '{money}', '{account}');"
    #     a.insert(dml)
    #     i += 1
    # print(i)
    # a.close_connect()
    # t4 = time.time()
    # print(t4 - t3)

    # 使用cursor.executemany 插入,executemany比execute快多了，executemany只用2秒左右就插完9万条，execute用了90多秒
    dml = "INSERT INTO `account`(`id`, `Name`, `Sex`, `Money`, `Account`) VALUES (%s, %s, %s, %s, %s);"
    t1 = time.time()
    count = a.insert_many(dml, [(id, random.choice(['王上', '赵小康', '李小强', 'Shaw', 'Mark', 'shabi', 'Python']),
                         random.choice(['男', '女']), random.uniform(1, 1000), random.randint(123456789, 999999999))
                        for id in range(9999, 99999)])

    a.con.commit()
    t2 = time.time()
    print(count)
    a.close_connect()
    print(t2 -t1)