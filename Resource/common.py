
from Resource.page import LoginPage


class DoubanBase(LoginPage):
    """
    豆瓣GUI自动化
    """
    def __init__(self, user, passwd, driver):

        LoginPage.__init__(self, driver)
        self.driver.implicitly_wait(10)
        self.url = 'https://www.douban.com'
        self.user = user
        self.passwd = passwd
        self.verificationErrors = []

    def _logout(self):
        self.driver.quit()

    def aw_login(self):

        self.open_login_page(self.url)
        self.max_window()  # 最大化浏览器窗口

        iframe = self.find_element(self.iframe[0], self.iframe[1])  # 处理iframe标签
        self.switch_to_iframe(iframe)  # 切换到真正的登录页面
        self.find_element(self.some_button[0], self.some_button[1]).click()

        self.input_user(self.user)
        self.input_passwd(self.passwd)
        self.submit()

    def aw_logout(self):
        self.driver.find_element_by_link_text("小飞飞的帐号").click()
        self.driver.find_element_by_link_text('退出').click()  # 推出登陆
        self._logout()



