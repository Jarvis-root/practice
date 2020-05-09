import unittest, threading, time
from HtmlTestRunner import HTMLTestRunner
from Resource import HTMLTestRunner

# suite = unittest.TestSuite()
discover = unittest.defaultTestLoader.discover('D:\\PycharmProjects\\Practice\\',
                                               pattern='douban_G*.py', top_level_dir='D:\\PycharmProjects\\')
tests = list()
for testSuite in discover:
    for testCase in testSuite:
        # suite.addTest(testCase)
        tests.append(testCase)  # 把用例放到列表里便于遍历
print(tests)


# 多线程运行测试
def run():
    tlist = list()
    f = open(r'D:\PycharmProjects\Practice\Report\Report-{}.html'.format(time.strftime('%Y-%m-%d-%M-%S')), 'wb')
    for i in tests:
        # runner = HTMLTestRunner(combine_reports=True)
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='自动化测试报告', description='Test Result：', verbosity=3)
        t = threading.Thread(target=runner.run, args=(i, ))
        tlist.append(t)

    for p in tlist:
        p.start()

    for p in tlist:
        p.join()
    f.close()


if __name__ == '__main__':
    run()
