import unittest

import time

from day5.myTestCase import MyTestCase
from day6.data_base.connectDB import connDb


class ZhuCeTest(MyTestCase):
    def test_zhu_ce(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name("username").send_keys("qiyuan888")
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("userpassword2").send_keys("123456")
        driver.find_element_by_name("mobile_phone").send_keys("15989789456")
        driver.find_element_by_name("email").send_keys("45677897967@qq.com")
        driver.find_element_by_class_name("reg_btn").click()
        time.sleep(5)

        #检查数据库中新增的记录的用户名和我们输入的用户名是否一致。
        expected = "qiyuan888"
        actual = connDb()[1]
        self.assertEqual(expected,actual)
        print(connDb()[1])
