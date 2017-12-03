import  unittest

if __name__ == '__main__':
    #默认测试用例加载器，用于寻找符合一定规则的测试用例。
    suite = unittest.defaultTestLoader.discover("./day5", pattern='*Test.py')
    #执行suite中的所有的测试用例
    #TextTestRunner 文本测试用例运行器TextTestRunner是一个类，后面加一个括号就是将类实例话，才能调用方法。
    unittest.TextTestRunner().run(suite)

