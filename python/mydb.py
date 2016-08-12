#!/usr/bin/python

import pymysql
import pymysql.cursors
import datetime
from datetime import timedelta

date = datetime.date.today() - timedelta(1)
impressions = 303113
spent=28.55

#Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='discrepancy_check',
                             charset='latin1',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `pubmatic` (`date`,`ssp`,`impressions`,`spent`) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, (date, 'pubmatic', impressions, spent))
    # connection is not autocommit by default. So you must commit to save your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `date`,`ssp`,`impressions`,`spent` FROM `pubmatic` WHERE `date`=%s"
        cursor.execute(sql, (date,))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
