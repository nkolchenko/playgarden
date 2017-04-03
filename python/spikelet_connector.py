#!/usr/bin/python

"""
Module which contains functions to pull SSP's data from SpikeLet.

"""

from __future__ import print_function
from itertools import islice

import json
import requests
import csv
import pymysql.cursors

#spikelet_host='spikelet.t5.va.us.strikead.com'

spikelet_port=9000
spikelet_url='http://{0}:{1}/report/v1/evaluate?token=staff'.format(spikelet_host,spikelet_port)

start_date='2017-03-29'
end_date='2017-03-30'

db_connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='discrepancy_check',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

def main_cycle():
    data=utc_fetch_from_spikelet(start_date, end_date)
    store_in_mysql(data)

def utc_fetch_from_spikelet(start_date, end_date):
    """
    It gets structure like:

    exchange,Date,Impressions,Media spent
    adconductor,2017-03-26,125610,132.2251738683044
    admeta,2017-03-26,11502,5.04064157976381
    ...

    """
    # UTC Exchanges
    json_template = """{
       "reports": [{
           "report": {
             "dimensions": [{"alias": "exchange", "column": "exchange" },
                            {"alias": "Date", "column": "event_day",
                                      "format": { "type": "date", "pattern": "YYYY-MM-dd" }}],
             "metrics":    [{"alias": "Impressions",
                                      "expression": { "op": "column", "column": "impressions", "aggregation": "sum" }},
                            {"alias": "Media spent",
                                      "expression": { "op": "column", "column": "media_spent", "aggregation": "sum" }}
                            ],
     "filters": [{ "kind": "exclude", "column": "exchange", "values": [ "nexage", "google", "rubicon", "smaato"]}
                        ],
             "orderedBy": [{ "field": "exchange", "order": "ASC" }]
           }
         }],
       "interval": { "start": "", "end": "", "tz": 0 },
       "format": "csv"
     }"""

    json_data = json.loads(json_template)
    json_data['interval']['start'] = start_date
    json_data['interval']['end'] = end_date

    # print(json_data)
    try:
        r = requests.post(spikelet_url,json=json_data)  # XXX:
        #print(r.text)
    except requests.exceptions.ConnectionError:
        print('Can\'t connect to http://{0}:{1} is it alive?'.format(spikelet_host,spikelet_port) )



    csv_data=r.content
    #print(csv_data)
    return csv_data

def store_in_mysql(csv_data):
    csv_lines = csv_data.splitlines()
    reader = csv.reader(csv_lines, delimiter=',')

    with db_connection,db_connection.cursor() as cursor:
        for row in islice(reader, 1, None):   # trick to get rid of leading row
        #for row in reader:
            date=row[1]
            ssp=row[0]
            impressions=row[2]
            spent_imp=row[3]
            query = """INSERT INTO strikead (date, ssp, impressions, spent_imp) VALUES ("{0}", "{1}", {2}, {3});"""
            sql = (query.format(date,ssp,impressions,spent_imp))
            print(sql)
            #cursor.execute(sql)
    db_connection.close()

if __name__ == '__main__':
    main_cycle()
