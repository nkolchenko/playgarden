#!/usr/bin/python
import pymysql.cursors
import uuid
import boto3

dir='/Users/nkolchenko/tmp/'
counter = 0

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
        print 'Uploading files: '
        for row in cursor:
#            print(row['id'])
            uid=uuid.uuid4()
            file_name = str(uid)+'.xml'
            path_name = str(dir)+str(file_name)
#            print dir+file_name
            with open(path_name , 'wb') as fo:
                fo.write(str(row['id']))
                fo.close()
            counter=counter+1
            print 'file '+str(counter)+' : '+str(file_name)
            s3_client = boto3.client('s3') #tried WITH here - no success
            s3_client.upload_file(path_name, 'strikead-vast-creatives', file_name)
            print 'Done'

finally:
    db_connection.close()

