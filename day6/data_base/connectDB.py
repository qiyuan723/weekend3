import pymysql
def connDb():
    #我们要想链接数据库，需要知道数据库的哪些信息：
    #ip地址，端口号 用户名 密码
    conn = pymysql.Connect(host="127.0.0.1",user="root",password="root",database="pirate",port=3306,charset="utf8")
    #查询hd_user表中所有的数据，并且倒叙打印。
    sql = "select * from hd_user order by id desc "
    #要想在代码中执行这条sql语句，首先要获得数据库的游标。
    curs = conn.cursor()
    curs.execute(sql)
    #想获取数据库中最新的记录
    #那么就要把数据库所有记录倒叙排序
    result = curs.fetchone()
    return result
if __name__ == '__main__':
    print(connDb())
