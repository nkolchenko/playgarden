#!/usr/bin/python

"""
Module which contains functions to pull SSP's data from SpikeLet.
"""

from __future__ import print_function

import csv
import json
from itertools import islice

import pymysql.cursors
import requests

spikelet_host_testing='1.spikelet.etl.t5.va.us.strikead.com'
spikelet_host='spikelet.p.va.us.strikead.com'

spikelet_port = 9000
spikelet_url = 'http://{0}:{1}/report/v1/evaluate?token=staff'.format(spikelet_host, spikelet_port)

# start_date = '2017-03-29'
# end_date = '2017-03-30'

def db_connection():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='discrepancy_check',
                                charset='utf8',
                                cursorclass=pymysql.cursors.DictCursor)


def main_cycle():
    data = utc_fetch_from_spikelet()
    #store_in_mysql(data)

def ad_hoc_fetch():
    """just put your query here"""
    json_template= """{
        "reports":[{
            "report":{
                "dimensions": [{"alias":"days",
                                "column":"event_day",
                                "format":{"pattern":"yyyy-MM-dd","type":"date"}
                               },
                               {"alias":"campaign_id",
                                "column":"campaign_id"
                               },
                               {"alias":"campaign_id_name",
                                "column":"campaign_name"
                                },
                                {"alias":"ad_id",
                                "column":"ad_id"},
                                {"alias":"ad_id_name",
                                "column":"line_item_name"},
                                {"alias":"currency_name","column":"currency_name"},
                                {"alias":"agency_id","column":"agency_id"}
                                ],
                "metrics":[{"alias":"media_spent_imp",
                            "expression":
                                {"op":"column",
                                 "column":"media_spent_cc",
                                 "aggregation":"sum"
                                 },
                "format":{  "type":"number",
                            "decimal_mark":".",
                            "precison":2,
                            "zero_represenation":"0"}
                            },{"alias":"total_spend",
                            "expression":{"op":"+",
                                         "left":{"op":"column","column":"media_spent_cc","aggregation":"sum"},
                                         "right":{"op":"+","left":{"op":"column","column":"system_margin_cc","aggregation":"sum"},
                                         "right":{"op":"+","left":{"op":"column","column":"agency_margin_cc","aggregation":"sum"},
                                         "right":{"op":"+","left":{"op":"column","column":"third_party_cost_1_cc","aggregation":"sum"},
                                         "right":{"op":"column","column":"third_party_cost_2_cc","aggregation":"sum"}}}}},
                            "format":{"type":"number","decimal_mark":".","precision":2,"zero_represenation":"0"}}],
                            "filters":[{"kind":"include","column":"agency_id","values":["3178","3042"]}],
                            "orderedBy":[{"field":"media_spent_imp","order":"DESC"}],
                            "schema":["days",
                                      "campaign_id",
                                      "campaign_id_name",
                                      "ad_id","ad_id_name",
                                      "currency_name",
                                      "media_spent_imp",
                                      "total_spend",
                                      "agency_id"]}
                                      }],
                            "interval":{"start":"2017-01-01 00:00","end":"2017-10-01 00:00","tz":0},"format":"csv"}"""

    json_data = json.loads(json_template)
    #json_data['interval']['start'] = start_date
    #json_data['interval']['end'] = end_date

    print(json_data)

    try:
        r = requests.post(spikelet_url, json=json_data)  # XXX:
        # print(r.text)
    except requests.exceptions.ConnectionError:
        print('Can\'t connect to http://{0}:{1} is it alive?'.format(spikelet_host, spikelet_port))

    csv_data = r.content
    print(csv_data)
    return csv_data


def utc_fetch_from_spikelet():
    """
    It gets structure like:

    exchange,Date,Impressions,Media spent
    adconductor,2017-03-26,125610,132.2251738683044
    admeta,2017-03-26,11502,5.04064157976381
    ...

    """
    # UTC Exchanges
    json_template1 = """{
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

    json_template = """
{
   "reports" : [
      {
         "report" : {
            "orderedBy" : [
               {
                  "field" : "agency_id",
                  "order" : "ASC"
               },
               {
                  "order" : "ASC",
                  "field" : "buying_type"
               },
               {
                  "order" : "ASC",
                  "field" : "impressions"
               }

            ],
            "schema" : [
               "agency_id",
               "buying_type",
               "impressions",
               "media_spent"
            ],
            "metrics" : [
               {
                  "alias" : "impressions",
                  "expression" : {
                     "op" : "column",
                     "aggregation" : "sum",
                     "column" : "impressions"
                  }
               },
               {
                  "expression" : {
                     "aggregation" : "sum",
                     "op" : "column",
                     "column" : "media_spent"
                  },
                  "alias" : "media_spent"
               }
            ],
            "filters" : [
               {
                  "kind" : "include",
                  "column" : "agency_id",
                  "values" : [
                     "676"
                  ]
               },
               {
                  "column" : "buying_type",
                  "kind" : "include",
                  "values" : [
                     "PMP",
                     "RTB"
                  ]
               }
            ],
            "dimensions" : [
               {
                  "column" : "agency_id",
                  "alias" : "agency_id"
               },
               {
                  "alias" : "buying_type",
                  "column" : "buying_type"
               }
            ]
         }
      }
   ],
   "interval" : {
      "start" : "2017-07-01",
      "end" : "2017-08-01",
      "tz" : 0
   },
    "format" : "csv"
}
            """

    json_data = json.loads(json_template)
    #json_data['interval']['start'] = start_date
    #json_data['interval']['end'] = end_date

    # print(json_data)
    try:
        r = requests.post(spikelet_url, json=json_data)  # XXX:
        # print(r.text)
    except requests.exceptions.ConnectionError:
        print('Can\'t connect to http://{0}:{1} is it alive?'.format(spikelet_host, spikelet_port))

    csv_data = r.content
    print(csv_data)
    return csv_data

def store_in_file():
    output_file='/Users/nkolchenko/spikelet_query_2017.out'
    with open(str(output_file), 'wb') as out_file:
        print('out_file: ' + str(output_file))
        cont=ad_hoc_fetch()
        out_file.write(cont)
        print('written')


def store_in_mysql(csv_data):
    csv_lines = csv_data.splitlines()
    reader = csv.reader(csv_lines, delimiter=',')

    with db_connection(), db_connection().cursor() as cursor:
        for row in islice(reader, 1, None):  # trick to get rid of leading row
            # for row in reader:
            date = row[1]
            ssp = row[0]
            impressions = row[2]
            spent_imp = row[3]
            query = """INSERT INTO strikead (date, ssp, impressions, spent_imp) VALUES ("{0}", "{1}", {2}, {3});"""
            sql = (query.format(date, ssp, impressions, spent_imp))
            print(sql)
            cursor.execute(sql)
    db_connection().close()


if __name__ == '__main__':
#    main_cycle()
    store_in_file()
