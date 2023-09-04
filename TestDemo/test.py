# from Resource import TestFrame
# from selenium import webdriver
# import time
#
#
# driver = webdriver.Chrome()
#
#
# class test_baidu_login(TestFrame):
#     def Prepare(self):
#         driver.get('https://www.baidu.com/')
#
#     def Procedure(self):
#         driver.find_element_by_name('wd').send_keys('hahaha')
#         time.sleep(3)
#         driver.find_element_by_id('su').click()
#         time.sleep(5)
#
#     def Cleanup(self):
#         driver.quit()


# class Mydemo(unittest.TestCase):
#
#
#     @classmethod
#     def setUpClass(cls):
#         pass
#     def test1(self):
#         '''登录'''
#         driver.get('https://www.baidu.com/')
#         driver.find_element_by_name('wd').send_keys('hahaha')
#
#         #do someting about login
#     def test2(self):
#         '''查询'''
#         driver.find_element_by_name('wd').send_keys('hahaha')
#         # do someting about search
#     def test3(self):
#         '''提交数据'''
#         driver.find_element_by_id('su').click()
#         # do someting about submmit
#
#     @classmethod
#     def tearDownClass(cls):
#         time.sleep(5)
#         driver.close()
#
# if __name__ == '__main__':
#     unittest.main()

class Pipe(object):
    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        def generator():
            for obj in other:
                if obj is not None:
                    yield self.func(obj)

        return generator()


@Pipe
def even_filter(num):
    return num if num % 2 == 0 else None


@Pipe
def multiply_by_three(num):
    return num * 3


@Pipe
def convert_to_string(num):
    return 'The Number: %s' % num


@Pipe
def echo(item):
    print(item)

    return item


def force(sqs):
    for item in sqs: pass


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

force(nums | even_filter | multiply_by_three | convert_to_string | echo)