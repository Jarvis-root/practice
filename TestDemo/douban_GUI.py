import unittest
import time
from Resource import common, HTMLTestRunner
from selenium import webdriver
from elog import aw_LogInfo

from BeautifulReport import BeautifulReport

#
# class TestDoubanlogin(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         user = 'q'
#         passwd = ''
#         driver = webdriver.Chrome()
#         cls.page = common.DoubanBase(user, passwd, driver)
#
#     def setUp(self):
#         pass
#
#     def test_login(self):
#         self.page.aw_login()
#         print('hhhhhh')
#
#     def tearDown(self):
#         self.page.aw_logout()
#         self.assertEqual([], self.page.verificationErrors)
#
#     @classmethod
#     def tearDownClass(cls):
#         pass


class TestDoubanbook(unittest.TestCase):
    def setUp(self):
        aw_LogInfo('现在可以记录日志了')
        self.driver1 = webdriver.Chrome()
        self.driver1.get('https://www.douban.com')

    def test_bk(self):
        """打开读书，这个会被HTMLTestRunner记录到报告中"""
        self.driver1.find_element_by_link_text('豆瓣读书').click()
        time.sleep(5)
        aw_LogInfo('hhahahahahahahah')

    def test_hh(self):
        aw_LogInfo('111111111222222')
        self.assertEqual(1,1)

    def tearDown(self):
        self.driver1.quit()
        aw_LogInfo('测试完毕')


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(TestDoubanlogin('test_login'))
    # suite.addTest(TestDoubanbook('test_bk'))
    # f = open(r'D:\PycharmProjects\Practice\Report\Report-{}.html'.format(time.strftime('%Y-%m-%d-%M-%S')), 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='自动化测试报告', description='Test Result：', verbosity=3)
    # runner.run(suite)
    # f.close()
    if __name__ == '__main__':
        test_suite = unittest.TestSuite((TestDoubanbook('test_bk'),TestDoubanbook('test_hh')))
        result = BeautifulReport(test_suite)
        result.report(filename='测试报告', description='测试deafult报告', log_path='report')








