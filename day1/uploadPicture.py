# 1.登录
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import time

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_name("userverify").submit()

# 2. 商品管理
driver.find_element_by_link_text("商品管理").click()
# 3.添加商品
driver.find_element_by_link_text("添加商品").click()

# 4.商品名称
# 有一种特殊的网页, 比如左边或者上边有一个导航条.这时就要注意了
# 开发很喜欢在一个页面中嵌套多个页面
# 其中"商品管理"和"添加商品"属于页面根节点的网页
# 商品名称属于frame框架里的子网页
# 之前讲过窗口切换, 用于不同网页之间的页面切换,
# 现在也是需要切花网页
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("iphone x")
# 5.商品分类
driver.find_element_by_xpath('//*[@id="1"]').click()
# driver.find_element_by_css_selector("#2")
driver.find_element_by_css_selector("[id='2']").click()
driver.find_element_by_id("6").click()
# driver.find_element_by_id("7").click()
# 双击是特殊的元素操作, 所有的特殊操作被封装到ActionChains这个类中
# java封装到Actions这个类中
# 链表必须以perform方法作为结尾
# 可以用来执行一组操作, 只要最后以perform()结束就可以了
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
# 6.商品品牌
brand = driver.find_element_by_name("brand_id")
Select(brand).select_by_index(1)

#点击商品图册
driver.find_element_by_link_text("商品图册").click()
#implicitily_wait 是用来判断整个页面是否加载完毕的
#有时页面加载完，但是javascript的控件还没有创建好，所以需要time.sleep,提高程序的稳定性。

#因为真正负责上传文件的页面元素是<input type="file">
#所以我们可以直接操作这个控件
#这个控件可以直接输入图片的路径
#\反斜杠是转义字符  正斜杠表示路径 或者用两个反斜杠
driver.find_element_by_name("file").send_keys("D:/555c5e038edde.jpg","D:/555c5e216944e.jpg")

#点击开始上传，同时使用三个class 定位
driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
#alert这个控件不是立刻弹出来的，需要等待，否则找不到
time.sleep(3)
driver.switch_to.alert.accept()

#继续添加
driver.find_element_by_name("file").send_keys("D:/555c5e216944e.jpg")
driver.find_element_by_css_selector(".uploadBtn.state-ready").click()
#alert这个控件不是立刻弹出来的，需要等待，否则找不到
time.sleep(3)
driver.switch_to.alert.accept()

# 7.提交
# brand.submit()
#页面太长，点击不了下面的button，怎么操作滚动条
#默认是0开始，到长度-1结束，range(10)表示0到9，一共10个数字
#没法拖动滚动条，使用向下箭头的方式实现向下拖动页面。
ac = ActionChains(driver)
for i in  range(10):
    ac.send_keys(Keys.ARROW_DOWN)
ac.perform()


driver.find_element_by_class_name("button_search").click()

