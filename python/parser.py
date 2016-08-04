#!/usr/bin/python

import csv
import datetime
from datetime import timedelta

check_date = datetime.date.today() - timedelta(2)
print("ololo "+str(check_date)+"\n")

with open('email.csv') as csvfile:
     reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
     for row in reader:
         if (row['Date']==str(check_date)):
            print(row['Date'],row['Paid Impressions'],row['Spend($)'])

#"Date", "Spend($)", "Paid Impressions"
#"2016-08-01", "40.73", "59593"
#"2016-08-02", "93.10", "101193"
#"Total", "133.83", "160786"



csvfile.close()