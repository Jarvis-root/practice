from Resource import page
from selenium import webdriver
from Resource.common import aw_LogInfo, aw_LogDebug


def aw_login(username, password):
    """

    :param username:
    :param password:
    :return:
    """
    aw_LogInfo('---- aw_LogInfo ----')
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    login_page = page.LoginPage(driver)
    login_page.open_login_page()
    login_page.input_user(username)
    login_page.input_passwd(password)
    login_page.submit()


