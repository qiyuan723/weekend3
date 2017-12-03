import unittest
from selenium import webdriver
import ddt

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from day4.readCsv2 import read

@ddt.ddt
class MemberManageTest(unittest.TestCase):
    #调用之前写好的read方法,获取配置文件中的数据。
    member_info = read("member_info.csv")
    driver = webdriver.Chrome()
    #在当前类只执行一次
    @classmethod
    def setUpClass(cls):#在所有方法之前都要执行一次，setUp只是执行第一次。
        print("所有方法之前，执行一次。")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):#在所有方法执行之后都要执行一次。
        time.sleep(2)
        print("这是teardown")
        #cls.driver.quit()

    def test_alogin(self):
        print("这是登录测试用例")
        driver = self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()

    #python中集合前面的星号表示，把集合中的所有元素拆开，一个一个写。
    #list=["abc","bcd"]
    #*list="abc","bcd"
    #假如一个方法需要接收两个参数，那么肯定不能传一个list进去。
    #但是如果list中正好也是两个元素，这时在列表前面加一个参数，
    #这时就不认为这是一个列表，而是两个参数。
    #@ddt.data()测试数据来源于read()方法
    @ddt.data(*member_info)
    def test_b_addmember(self,row):
        #每组测试数据就是一组测试用例，每条测试用例都是独立的。不能因为上一条测试数据失败，导致下一组数据不能被正常执行。所以这里不推荐用for循环。
        #应该用ddt装饰器 去修饰这个方法 达到测试用例每条独立执行的目的。ddt是数据驱动测试。data driver test
        #注释掉for循环，改变代码的缩进。

       #for row in read("member_info.csv"):
        print("这是添加会员方法")
        driver = self.driver
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        iframe_css = "#mainFrame"
        #如果frame没有name属性时，我们可以通过其他定位iframe标签，把定位好的页面元素传给switch to
        iframe_html = driver.find_element_by_css_selector(iframe_css)
        driver.switch_to.frame(iframe_html)
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        driver.find_element_by_css_selector('[value='+'"'+ row[2]+'"' +']').click()  #'[value="0"]''"[value="+row[2]+"]"'
        driver.find_element_by_name("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()

        #此处需要加断言，只能自动运行，但是不能自动判断是否对。
        actual = driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text
        expected = row[0]
        #断言类似于 if 。。。else。。。。是用来做判断的。
        if (actual==expected):
            print ("测试通过")
        else:
            print("测试失败")
        # 断言和if优缺点比较,断言是框架提供的，要想调用断言，那么必须加self.,因为测试用例类继承了框架中的testcase类，也继承了这个类中的断言。所以我们可以直接用断言的方法。
        #断言比较简短，断言只关注错误的测试用例，只有判断为假的时候才会打印信息，正确无信息输出。断言失败，下面的代码将不再执行。
        self.assertEqual(actual,expected)

        #切换到父框架
        driver.switch_to.parent_frame()

if __name__ == '__main__':
    unittest.main()



