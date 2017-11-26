import pymysql.cursors,os
import configparser

baseDir = os.path.dirname(__file__)
baseDir = str(baseDir)
baseDir = baseDir.replace('\\','/')
base = baseDir.split("/mysqlDb")[0]
filePath = base + '/dbConfig.ini'
# 读取配置文件
cf = configparser.ConfigParser()
cf.read(filePath,encoding=None)
host = cf.get('mysqlconf','host')
port = cf.get('mysqlconf','port')
db = cf.get('mysqlconf','dbName')
user = cf.get('mysqlconf','user')
password = cf.get('mysqlconf','password')
# print(host,port,db,user,password)
class DB():
    def __init__(self):
        try:
            self.connection = pymysql.connect(host=host,
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor
                                              )
        except pymysql.err.OperationalError as e:
            print("数据库连接不成功,错误如下：")
            print('mysql Error %d:%s'%(e.args[0],e.args[1]))
        else:
            pass
        finally:
            pass
    #清空数据表
    def clearTable(self,table_name):
        sql = "truncate table" + " " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            self.connection.commit()
    #删除数据
    def delData(self,table_name,column_name,value):
        #delete from table where id = "1";
        sql = "delete from " + table_name + " where " + column_name + " = " + value + ";"
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            self.connection.commit()
    #关闭数据库连接
    def close(self):
        self.connection.close()
    #查询数据
    def selectData(self,table_name):
        #select * from table where column_name = '';
        sql = "select * "+" from" + " " + table_name +";"
        # print(sql)
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            # fetchall()获取所有结果集，返回是一个列表，
            result = cursor.fetchall()
            self.connection.commit()
        return result
    #插入数据
    def insertData(self,table_name,test_data):
        for i in test_data:
            test_data[i] = "'" + str(test_data[i]) + "'"
        key = ",".join(test_data.keys())
        value = ",".join(test_data.values())
        sql = "insert into " + table_name + " ( " + key + " ) " + " values " + " ( " + value+ " ) " + ";"
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            self.connection.commit()
if __name__ == "__main__":
    db = DB()