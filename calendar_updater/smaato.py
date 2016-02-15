#!/usr/local/bin/python

import _mysql
import datetime
from datetime import timedelta

check_date = datetime.date.today() - timedelta(2) # нам надо инфа за прошедшую дату
#check_date=20160213
#print check_date

my_date = check_date.strftime('%Y%m%d')
#my_date = str(my_date)
#print my_date

#открываю конекшн
cnx = _mysql.connect(user='root', passwd='',
                              host='127.0.0.1',
                              db='strikead')

#готовлю SELECT statement
my_query="select * from strikead where date="+my_date

#стреляю
cnx.query(my_query)
r=cnx.store_result()

print str(r.fetch_row(maxrows=0))


cnx.close()

