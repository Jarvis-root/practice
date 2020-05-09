import unittest
from selenium import webdriver
from selenium.webdriver import support
import time


driver = webdriver.Chrome()


class test_baidu_login(unittest.TestCase):
    def setUp(self):
        driver.get('https://www.baidu.com/')

    def test_hhh(self):
        driver.find_element_by_name('wd').send_keys('hahaha')
        time.sleep(3)
        driver.find_element_by_id('su').click()
        time.sleep(1)
        # self.assertEqual(1, 2)

    def tearDown(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main()