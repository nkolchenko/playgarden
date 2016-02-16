#!/usr/local/bin/python

#import _mysql
import sys
import datetime
from datetime import timedelta
import MySQLdb
import smtplib

check_date = datetime.date.today() - timedelta(2)
my_date = check_date.strftime('%Y%m%d')


connection = MySQLdb.connect (host = "localhost", user = "root", db = "strikead")
cursor = connection.cursor ()

my_query="select * from strikead where date="+my_date



cursor.execute(my_query)
data = cursor.fetchall ()

for row in data :
    message_2 = "\n"\
         "date: "+str(row[0])+"\n"\
         "bids: "+str(row[6])+"\n"\
         "impressions: "+str(row[2])+"\n"\
         "media_spent: "+str(row[3])+"\n"

cursor.close ()
connection.close ()



sender = 'from@fromdomain.com'
receivers = ['nikolay@localhost']

message_1 = """From: Nikolay <nikolay@localhost>
To: nikolay@localhost

Subject: Our daily statistic for Smaato for: """+str(check_date)+""".
"""

message = str(message_1)+str(message_2)
print message

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"

sys.exit()