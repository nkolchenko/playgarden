#!/usr/bin/python

import os.path
import csv
import datetime
from datetime import timedelta
import pymysql as mdb

date = datetime.date.today() - timedelta(3)
def pubmatic(date):

#    check_date = datetime.date.today() - timedelta(3)
#    underscored=datetime.datetime.strptime(str(check_date), '%Y-%m-%d').strftime('%Y_%m_%d')

    path = './'
    report_file='{path}pubmatic_{date}.csv'.format(path=path,
                                                   date=date.strftime('%Y_%m_%d'))

    if not os.path.isfile(report_file):
        print("Warning! No Pubmatic csv for {date}".format(date=date))

    else:
        print(str(report_file))
        with open(report_file) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                if (row['Date'] == str(date)):
                    print(str('ok'))
                    return(row['Date'],
                          'pubmatic',
                          float(row['Spend($)']),
                          int(row['Paid Impressions']))

if __name__ == '__main__':
    pubmatic(date)

