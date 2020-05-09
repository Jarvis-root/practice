from Resource.html_test_runner import HTMLTestRunner
from Resource.log import logger
import unittest
import time


loader = unittest.TestLoader()
suite = loader.discover('D:\PycharmProjects\Practice\TestDemo')


if __name__ == '__main__':
    f = open(r'D:\PycharmProjects\Practice\Report\Report-{}.html'.format(time.strftime('%Y-%m-%d-%M-%S')), 'wb')
    runner = HTMLTestRunner(stream=f, title='自动化测试报告', description='Test Result：', verbosity=3)
    runner.run(suite)
    f.close()
