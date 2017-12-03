#1.之前的readCsv不能被其他测试用例调用，应该给这段代码封装到一个方法里。
#2.每个测试用例的路径不同，所以path应该作为参数传到到这个方法中
#3.打开了一个文件并没有关闭。会造成内存泄露最终可能内存泄露。
import csv
import os


def read(file_name):
    #所有的重复代码的出现，都是程序设计的不合理。
    #重复的代码应该封装到一个方法里。
    current_file_path = os.path.dirname(__file__)
    path = current_file_path.replace("day4", "data/"+file_name)
    #file = open (path,"r")
    #with代码块可以自动关闭with中声明的变量。
    result = []
    with open(path,"r") as  file:
        data_table = csv.reader(file)
        for row in data_table:
            result.append(row)
            #print (row)
    return result
    #如果在打开和关闭程序的代码之间，发生了异常情况，导致后面的代码不能正常执行，
    #file.close()也不执行，这时，文件仍然不能关闭。
    #应该用with.....as.....语句实现文件的关闭
    #file.close()

if __name__ == '__main__':
   # path = r"C:\Users\51Testing\PycharmProjects\weekend3\data\member_info.csv"
#这个路径是绝对路径，我们工作中，一个项目不只一个人编写代码。
    #所以应该在代码中，通过当前代码文件的路径，根据相对位置，自动找到相对路径。os操作系统 path路径  dir是directory目录
   #__file__是pathon内置的变量，指的就是当前文件。

    member_info = read("member_info.csv")

    print ((member_info)[0])
   #读出数据不是目的，目的是通过数据驱动测试，所以应该把数据作为方法的返回值作为调用





