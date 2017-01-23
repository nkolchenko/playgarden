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
    with db_connection.cursor() as cursor:
        sql = "SELECT `id` FROM `creative` limit 2"
        cursor.execute(sql)
        for row in cursor:
            #print(row)
            uid=uuid.uuid4()
            file_name = str(uid)+'.xml'
            #print dir+file_name
            file = open('file_name' , 'wb')
            file.write(str(row));
            file.close()

finally:
    db_connection.close()

