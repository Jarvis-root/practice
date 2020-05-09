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
import unittest


def test():
    assert  2 > 3

a = unittest.FunctionTestCase(test)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(a)
