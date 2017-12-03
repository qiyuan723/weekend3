import  unittest
from selenium import webdriver
import time


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()