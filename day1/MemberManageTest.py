import unittest
from selenium import webdriver

import time


class MemberManageTest(unittest.TestCase):
    #变量前面加上self，表示这个变量是类的属性。
    def setUp(self):
        #打开浏览器
        #driver声明在setUp方法之内，不能被其他方法访问。
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()#如果浏览器升级了，该句需要注释。

    def tearDown(self):
        time.sleep(20)
        self.driver.quit()
        #quit退出整个浏览器
        #close关闭当前标签
        #代码编写和调试的时候需要在quit()方法前加一个时间等待。正式运行的时候需要注释掉时间等待。
    def test_add_member(self):
        driver = self.driver
        driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_name("userverify").submit()
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys("test")
        driver.find_element_by_name("mobile_phone").send_keys("15987456689")
        driver.find_element_by_css_selector('[value="0"]').click()
        driver.find_element_by_name("birthday").send_keys("2017-11-25")
        driver.find_element_by_name("email").send_keys("432432432@qq.com")
        driver.find_element_by_class_name("button_search").click()























