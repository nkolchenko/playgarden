#!/usr/local/bin/python

#import _mysql
import sys
import datetime
from datetime import timedelta
import MySQLdb


check_date = datetime.date.today() - timedelta(2)
my_date = check_date.strftime('%Y%m%d')


connection = MySQLdb.connect (host = "localhost", user = "root", db = "strikead")
cursor = connection.cursor ()

my_query="select * from strikead where date="+my_date

cursor.execute(my_query)
data = cursor.fetchall ()

for row in data :
    print "Sizmek's daily statistic for Smaato\n"\
          "date: "+str(row[0])+"\n"\
          "bids: "+str(row[6])+"\n"\
          "impressions: "+str(row[2])+"\n"\
          "media_spent: "+str(row[3])+"\n"\

cursor.close ()
connection.close ()

sys.exit()