from selenium import webdriver
from selenium.webdriver.common.by import By

import time

from day5.myTestCase import MyTestCase
from day6.page_object.loginPage import LoginPage
from day6.page_object.personalCenterPage import PersonalCenterPage


class LoginTest(MyTestCase):
    def test_login(self):
        #现在这种测试用例可读性比较差，维护起来比较困难。
        #那测试用例写成什么样可读性比较好呢。
        #打开网页
       # self.driver.get("http://localhost/index.php?m=user&c=public&a=login")
        lp =  LoginPage(self.driver)#实例化一个登录页面
        lp.open()
        #输入用户名 密码
        #self.driver.find_element(By.ID,"username").send_keys("qiyuan")
        lp.input_username("qiyuan")
        #self.driver.find_element(By.ID,"password").send_keys("123456")
        lp.input_password("123456")
        #点击登录
        #self.driver.find_element(By.CLASS_NAME,"login_btn").click()
        lp.click_login_button()
        time.sleep(3)
        #验证是否跳转到管理中心页面
        #标题  网址  页面元素
        #expected = "我的会员中心 - 道e坊商城 - Powered by Haidao"
        #actual = self.driver.title
        #self.assertEqual(expected,actual)

        pcp = PersonalCenterPage()#创建一个个人中心实例
        time.sleep(5)
        self.assertEqual(pcp.title,self.driver.title)






