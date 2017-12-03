import  unittest
from selenium import webdriver

import time

from day5.myTestCase import MyTestCase


class DengLuTest(MyTestCase):
    """登录模块的测试用例"""
    def test_denglu(self):
        """登录测试正常情况测试用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("qiyuan")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("password").submit()
        print("当前用户名：qiyuan")

