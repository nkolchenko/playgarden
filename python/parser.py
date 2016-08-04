#!/usr/bin/python

import csv
import datetime
from datetime import timedelta

check_date = datetime.date.today() - timedelta(10)
underscored=datetime.datetime.strptime(str(check_date), '%Y-%m-%d').strftime('%Y_%m_%d')

with open('pubmatic_'+str(underscored)+'.csv') as csvfile:
     reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
     for row in reader:
         if (row['Date'] == str(check_date)):
             print(row['Date'], row['Paid Impressions'], row['Spend($)'])

#""
#"Date", "Spend($)", "Paid Impressions"
#"2016-08-01", "40.73", "59593"
#"2016-08-02", "93.10", "101193"
#"Total", "133.83", "160786"

csvfile.close()


#query = '''INSERT INTO {ssp} (date, ssp, impressions, spent)
#           VALUES ("{date}", "{ssp}", {impressions}, {spent});'''
#con = mdb.connect('localhost', 'root', '', 'discrepancy_check')
#cur = con.cursor()

#try:
#    cur.execute(query.format(date=data[0],
#                             ssp=data[1],
#                             impressions=data[2],
#                             spent=data[3]))
#    con.commit()

#except:
#    con.rollback()

#con.close()


