#!/usr/bin/python
import pymysql.cursors
import uuid
import boto3
import requests
import botocore.session

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
        sql = "SELECT `id` FROM `creative` limit 1"
        cursor.execute(sql)
        print 'Uploading files: '
        for row in cursor:
            uid=uuid.uuid4()
            file_name = str(uid)+'.xml'
            path_name = str(dir)+str(file_name)
            with open(path_name , 'wb') as fo:
                fo.write(str(row['id']))
                fo.close()
            counter=counter+1
            print 'file '+str(counter)+' : '+str(file_name)

            with open(path_name, 'r') as fo:
                 content = fo.read(10)
                 fo.close()
            s3 = boto3.resource('s3')
            s3_client = boto3.client('s3')
            s3.Bucket('strikead-vast-creatives').put_object(ACL='public-read',Body=content,
                                                            Key=file_name,ContentType='text/xml')

            url = s3_client.generate_presigned_url(ClientMethod='get_object',Params={'Bucket': 'strikead-vast-creatives',
                                                                              'Key': file_name})
            response = requests.get(url)
            url_part = url.split('?')
            url_part = url_part[0]
            print 'Uploaded to: '+str(url_part)

finally:
    db_connection.close()

