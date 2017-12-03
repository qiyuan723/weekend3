#测试框架是干什么用的
#最主要的用途是组织和执行测试用例
#1.导入unittest框架
import unittest
#java中类和文件名的关系，如果是Public类型的，那么类名和文件名一样。
#python中可以一样，但是推荐：文件名首字母小写。类名首字母大写。剩下一样
#2.要继承unittest中的父类，
#python中的继承直接用小括号表示

#TestCase是测试用例的意思，我们就在UnittestDemo中编写测试用例。
class UnittestDemo(unittest.TestCase):
    #3.重写父类中的方法setUp和teardown
    #def是方法的关键字
    #setUp是创建的意思
    #类似于手动测试中的预置条件
    def setUp(self):#打开浏览器
        print("这个方法将会在测试用例执行前先执行")

    def tearDown(self):#关闭浏览器，类似于还原测试环境。
        print("这个方法将会在测试用例方法之后执行")
#4.编写测试用例方法
    #只有以test开头命名的方法才是测试用例方法
    #测试用例方法，可以直接被运行
    #普通方法不能直接被执行，
    def test_login(self):
        print("登录测试用例")
        self.zhe_ce()
    def zhe_ce(selfself):
        print("注册测试用例")
    def test_search(self):
        print("搜索测试用例")
    #执行哪个函数跟鼠标的位置相关。
    #如果直接执行这个文件，那么就会执行下面的语句，否则
    #从其他文件中调用该文件的时候，import该文件的时候，下面的代码就不会被执行。
if __name__ == '__main__':
    #执行当前文件中所有的unittest的测试用例。
    #unittest.main()
    UnittestDemo.zhu_ce()









