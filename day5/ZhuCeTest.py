#有了myTestCase之后，再写测试用例就不需要重新写setUp和tearDown方法。
import os
from selenium import webdriver
from day5.myTestCase import MyTestCase


class ZheCeTest(MyTestCase):
    #三个双引号，表示文档字符串，也是一种注释，和#的区别就是这种会显示在文档中。
    """注册模块测试用例"""
    #因为myTestCase已经实现了setUP和tearDown方法，我们以后再写测试用例就不需要重新实现setup和teardown。
    def test_zhu_ce(self):
        """打开注册页面的测试用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        #driver.current_url#用来获取当前浏览器中的网址
        actual = driver.title#用来获取当前浏览器中的标签页的title
        expected = "用户注册 - 道e坊商城 - Powered by Haidao"
        base_path = os.path.dirname(__file__)#
        path = base_path.replace("day5","report/image/")
        driver.get_screenshot_as_file(path + "注册.png")
        self.assertEqual(actual, expected)  # 断言成功了不返回任何消息
