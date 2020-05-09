from selenium.webdriver.common.by import By
from elog import aw_LogDebug


class Page(object):
    """
       基本类，用于所有页面的继承
    """

    def __init__(self, driver, url='....'):

        self.driver = driver
        self.main_url = url
        self.timeout = 30

    def open_url(self, url):
        if url:
            new_url = self.main_url + url
        else:
            new_url = self.main_url

        if self.driver.get(new_url):
            aw_LogDebug('打开页面:{}'.format(new_url))

    def find_element(self, by, value):
        """

        :param by: eg. By.ID
        :param value: 标签的值
        :return:
        """
        return self.driver.find_element(by, value)

    def script(self, src):
        return self.driver.execute_script(src)

    def max_window(self):
        return self.driver.maximize_window()

    def switch_to_iframe(self, iframe):
        """
        切换到指定的iframe
        :param iframe:
        :return:
        """
        return self.driver.switch_to.frame(iframe)

    def switch_to_parent_iframe(self):
        """
        回到上一级ifame
        :return:
        """
        return self.driver.switch_to.parent_frame()

    def switch_to_default_frame(self):
        """
        回到默认iframe
        :return:
        """
        return self.driver.switch_to.default_content()

    def switch_to_alert(self):
        """
        切到提示框
        :return:
        """
        return self.driver.switch_to.alert()

    def switch_to_active_element(self):
        """
        从提示框切回
        :return:
        """
        return self.driver.switch_to.active_element()

    def send_keys(self, by, value, send_value, clear_first=True, click_first=False, ):
        """

        :param by:
        :param value:
        :param send_value:
        :param clear_first:
        :param click_first:
        :return:
        """
        try:
            # args = getattr(self, '_%s' % args)
            if click_first:
                self.find_element(by, value).click()
            if clear_first:
                self.find_element(by, value).clear()

            self.find_element(by, value).send_keys(send_value)
        except Exception:
            aw_LogDebug('%s 方法未定位到元素%s ') % (by, value)

    def wait_for_element(self, by, ele, timeout=10):
        """

        :param by: eg. By.ID
        :param ele: element
        :param timeout:
        :return:
        """
        while timeout:
            try:
                if self.find_element(by, ele):
                    return self.find_element(by, ele)
            finally:
                timeout -= 2


class LoginPage(Page):
    """
    登录页面
    """
    def __init__(self, driver):
        Page.__init__(self, driver=driver)

        # 定位器
        self.username_input = [By.XPATH, '//*[@id="username"]']
        self.password_input = [By.XPATH, '//*[@id="password"]']
        self.submit_button = [By.LINK_TEXT, '登录豆瓣']
        self.iframe = [By.XPATH, '//*[@id="anony-reg-new"]/div/div[1]/iframe']
        self.some_button = [By.XPATH, '/html/body/div[1]/div[1]/ul[1]/li[2]']

    def open_login_page(self, url):
        self.open_url(url)

    def input_passwd(self, password):
        self.send_keys(self.password_input[0], self.password_input[1], password)

    def input_user(self, username):
        self.send_keys(self.username_input[0], self.username_input[1], username)

    def submit(self):
        self.find_element(self.submit_button[0], self.submit_button[1]).click()
