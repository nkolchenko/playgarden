#!/usr/bin/python
import pymysql.cursors
import uuid
import boto3

counter = 0
s3 = boto3.resource('s3')

db_connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='strikead',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with db_connection, db_connection.cursor() as cursor:
        sql = "SELECT id, tracking_code FROM creative WHERE creative_type_id = 5 AND (vast_url IS NULL OR vast_url = '')"
        cursor.execute(sql)
        print 'Uploading files: '
        for row in cursor:
            uid = uuid.uuid4()
            key_name = str(uid)+'.xml'
            i_creative = str(row['id'])
            tracking_code = str(row['tracking_code'])
#            print tracking_code
#            print i_creative
#            print key_name

            s3.Bucket('strikead-vast-creatives').put_object(ACL='public-read',Body=tracking_code,
                                                            Key=key_name,ContentType='text/xml')

            url = 'https://strikead-vast-creatives.s3.amazonaws.com/'+str(key_name)
            counter = counter+1
            print 'Creative: '+str(i_creative)+' has been uploaded to: '+str(url)
            with db_connection, db_connection.cursor() as cursor2:
                sql2 = 'UPDATE `creative` SET vast_url="%s" where id=%s' %(url , i_creative)
#                print 'Updating DB wth: '+str(sql2)
                cursor2.execute(sql2)
#                print 'updated DB'

finally:
    db_connection.close()
    print '\n '+str(counter)+' Files uploaded'

