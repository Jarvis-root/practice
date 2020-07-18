import pytest

# pytest可以使用allure来生成报告
# pytest --alluredir=D:\PycharmProjects\practice\TestDemo\allure using_pytest_with_allure.py

# 查看报告
# allure serve D:\PycharmProjects\practice\TestDemo\report


def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')