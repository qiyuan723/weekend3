#1.要读CSV文件，首先要准备一个CSV文件
#2.导入CSV的包
#csv是python语言内置的包，说明比selenium常用。开发和测试都常用。
import csv

#要想读取csv文件，需要知道其路径
#字符串前加r说明该字符串中没有转义字符。说明反斜杠是普通字符，不看做转义字符。
path = r"C:\Users\51Testing\PycharmProjects\weekend3\data\member_info.csv"

#要想读内容，需要通过路径打开文件。file就是文件的内容
file = open(path,"r")
#4.通过csv代码库，读取csv格式的内容
data_table = csv.reader(file)
#遍历data_table,分别打印每一行数据。
for row in data_table:
    print(row)









