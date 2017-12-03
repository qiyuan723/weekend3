#1.登录
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("qiyuan")
ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
driver.find_element_by_link_text("账号设置").click()
driver.find_element_by_partial_link_text("个人资料").click()
#clear是清空的意思，用来清空元素中原本的内容
#更好的编程习惯是在每次执行sendkeys之前，都进行一遍clear操作。
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("测试")
#css可以用多个属性组合定位一个元素
#一个元素的多个属性之间不能用空格
driver.find_element_by_css_selector('#xb[value="1"]').click()
driver.execute_script('document.getElementById("date").removeAttribute("readonly")').clear()
driver.find_element_by_id("date") .send_keys("2017-11-24")
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("657894562")
driver.find_element_by_class_name("btn4").click()
#这种右键检查不出来的html代码的弹出框，叫做alert，有单独的方法来处理
#alert控件不是html代码生成的，所以implicitly_wait对这个控件不管用。
#所以需要写time.sleep,所以组合使用。
time.sleep(3)
driver.switch_to.alert().accept()
#alert 弹出框，accept 接受，同意，确定
#切换到alert的方法和切换到窗口的方法一致。
#2.点击账号设置
#3.点击个人资料
#4.修改个人信息
#5.用arguments写输入

