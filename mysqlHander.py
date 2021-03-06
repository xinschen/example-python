#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
u'''
对常用数据库操作进行类封装
'''
import re
import pymysql as mysql

class MySQL:
    u'''对MySQLdb常用函数进行封装的类'''
    error_code = '10023' #MySQL错误号码

    _instance = None #本类的实例
    _conn = None # 数据库conn
    _cur = None #游标

    _TIMEOUT = 30 #默认超时30秒
    _timecount = 0

    def __init__(self, dbconfig):
        u'构造器：根据数据库连接参数，创建MySQL连接'
        try:
            self._conn = mysql.connect(host=dbconfig['host'],
                     port=dbconfig['port'], 
                     user=dbconfig['user'],
                     passwd=dbconfig['passwd'],
                     db=dbconfig['db'],
                     charset=dbconfig['charset'])
        except mysql.Error as e:
            self.error_code = e.args[0]
            error_msg = 'MySQL error! ', e.args[0], e.args[1]
            print (error_msg)
            #如果没有超过预设超时时间，则再次尝试连接，
            if self._timecount < self._TIMEOUT:
                interval = 5
                self._timecount += interval
                time.sleep(interval)
                return self.__init__(dbconfig)
            else:
                raise Exception(error_msg)
    
        self._cur = self._conn.cursor()
        self._instance = mysql

    def title(self,sql):
        u'获取sql中的中文列名'
        if re.findall("CONCAT",sql):
            tmp_title = sql.split('SELECT')[1].split('FROM')[0].split(',')
            title = [ i.split()[-1] for i in tmp_title if not re.findall("CONCAT",i) ]
        else:
            title = [ i.split()[-1] for i in sql.split('SELECT')[1].split('FROM')[0].split(',')  ]
        return title


    def query(self,sql):
        u'执行 SELECT 语句'  
        try:
            self._cur.execute("SET NAMES utf8") 
            result = self._cur.execute(sql)
        except mysql.Error as e:
            self.error_code = e.args[0]
            print ("数据库错误代码:",e.args[0],e.args[1])
            result = False
        return result

    def update(self,sql):
        u'执行 UPDATE 及 DELETE 语句'
        try:
            self._cur.execute("SET NAMES utf8") 
            result = self._cur.execute(sql)
            self._conn.commit()
        except mysql.Error as e:
            self.error_code = e.args[0]
            print ("数据库错误代码:",e.args[0],e.args[1])
            result = False
        return result

    def insertOneData(self,sql):
        u'执行 INSERT 语句。如主键为自增长int，则返回新生成的ID'
        try:
            self._cur.execute("SET NAMES utf8")
            self._cur.execute(sql)
            self._conn.commit()
            return self._conn.insert_id()
        except mysql.Error as e:
            self.error_code = e.args[0]
            return False
    def insertManyData(self,sql,tupledata):
        u'执行多条INSERT数据'
        try:
            self._cur.execute("SET NAMES utf8")
            self._cur.execute(sql,tupledata)
            self._conn.commit()
            return self._conn.insert_id()
        except mysql.Error  as e:
            self.error_code = e.args[0]
            return False   
  
    def fetchAllRows(self):
        u'返回结果列表'
        return self._cur.fetchall()

    def fetchOneRow(self):
        u'返回一行结果，然后游标指向下一行。到达最后一行以后，返回None'
        return self._cur.fetchone()
 
    def getRowCount(self):
        u'获取结果行数'
        return self._cur.rowcount
              
    def commit(self):
        u'数据库commit操作'
        self._conn.rollback()
       
    def __del__(self): 
        u'释放资源(系统GC自动调用)'
        try:
            self._cur.close() 
            self._conn.close() 
        except:
            pass
    
    def close(self):
        u'关闭数据库连接'
        self.__del__()

