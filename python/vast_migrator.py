#!/usr/bin/python
import pymysql.cursors
import uuid

dir='/Users/nkolchenko/tmp/'

db_connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='strikead',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


try:
    with db_connection, db_connection.cursor() as cursor:
        sql = "SELECT `id` FROM `creative` limit 2"
        cursor.execute(sql)
        for row in cursor:
#            print(row['id'])
            uid=uuid.uuid4()
            file_name = str(dir)+ str(uid)+'.xml'
            #print dir+file_name
            with open(file_name , 'wb') as fo:
                fo.write(str(row['id']))
                fo.close()

finally:
    db_connection.close()

