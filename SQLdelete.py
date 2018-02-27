#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","123456","test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)

try:
    # 执行语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 报错时回滚
    db.rollback()

# 关闭数据库连接
db.close()