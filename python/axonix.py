#!/usr/bin/python

import csv
import os.path
import datetime
from datetime import timedelta

date = datetime.date.today() - timedelta(4)

path = './'
report_file='{path}sizmek.csv'.format(path=path,)
sum_revenue=0
sum_impressions=0

if not os.path.isfile(report_file):
    print("Warning! No axonix csv for {date}".format(date=date))

#"network","date","requests","impressions","impressionrate","revenue"
#"Sizmek (StrikeAd) ROW","2016-08-05","323562","283071","0.874858605151408","478.33182"
#"Sizmek (StrikeAd) US","2016-08-05","220281","199751","0.906800858902947","374.75826"


else:
    print(str(report_file))
    with open(report_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            if (row['date'] == str(date)):
#                print(str('ok'))
                sum_revenue += float(row['revenue'])
                sum_impressions += int(row['impressions'])

        print(str(date),
                'axonix',
                sum_revenue,
                sum_impressions)

#if __name__ == '__main__':
#   pubmatic(date)
