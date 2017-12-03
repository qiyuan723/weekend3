import os
import smtplib
import unittest

#HTMLTestRunner是基于Unittest框架的一个扩展，可以在网上搜索下载，这个是Python3
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    f = open(path,"rb")#二进制的方式读取
    mail_body=f.read()
    f.close()
    #要想发邮件，我们要把二进制的内容转成MIME格式
    #MIME 多用途，互联网，邮件，扩展
    #这种格式是对邮件协议的扩展，使邮件不仅支持文本格式，还支持多种格式。比如图片、音频、二进制文件。
    msg = MIMEText(mail_body,"html","utf-8")#正文
    #上面是邮件的正文，但是对于一个邮件来讲，除了正文，还需要主题，发件人，收件人。
    #msg是字典的类型，字典类似于数组。区别：字典是无序的。
    #dict = {}
    msg["Subject"] = Header("自动化测试报告--齐小缘儿","utf-8")

    #如果 想用客户端软件或者自己写代码登录邮箱，很多类型的邮件需要单独设置一个客户端授权，为了邮箱安全着想
    #因为你们都没有设置授权码，所以发件箱用我的
    msg["From"] = "bwftest126@126.com"
    msg["To"] = "qiyuan723@126.com"
    #邮件内容已经准备好了，下面开始发送邮件。
    #发邮件的手动步骤：
    #1.打开登录


    #首先导入smtplib的代码库
    smtp = smtplib.SMTP() #实例化一个SMTP类的对象
    smtp.connect("smtp.126.com")#链接126邮箱的服务器地址
    #2.登录邮箱
    smtp.login("bwftest126@126.com","abc123asd654")
    #3.发送邮件
    smtp.sendmail(msg["From"],msg["To"],msg)
    #4.退出邮箱
    smtp.quit()
    print("邮件发送成功了")

if __name__ == '__main__':
    #时间戳 str是字符串 f是格式 time是时间
    #strftime()通过这个方法可以定义时间的格式。

    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    time.sleep(1)

    suite = unittest.defaultTestLoader.discover("./day5","*Test.py")
    #htmld的测试用例运行器最终会生成一个html格式的测试报告
    #我们是不是至少要指定测试报告的路径啊
    base_path =  os.path.dirname(__file__)
    path = base_path + "/report/report" + now + ".html"
    file = open(path,"wb")
    HTMLTestRunner(stream=file, title="齐小缘的测试报告", description="运行环境：windows 7 谷歌54版本浏览器  用例包括：登录、注册").run(suite)
    file.close()



    #我们要把html报告作为邮件正文，发送给boss
    send_mail(path)
    #这时生成的测试报告，只显示类名和方法名，只能给专业人士看。
    #我们应该把相关的手动测试用例的标题加到我们的报告里。
    #我们自动化测试用例是从手工测试用例中挑选出来的，手工测试用例怎么写我们就怎么写。
    #新的测试报告会覆盖原来的测试报告，如果想把所有的测试报告保存起来
    #加一个时间戳，按照当前时间计算一个数字，把数字作为文件名的一部分，避免了文件名重复的问题。
    #现在我们的html格式的测试报告生成了，当测试用例全部执行完成，我们应该生成一封提醒邮件。通知所有关心测试结果的人。






