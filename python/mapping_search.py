#!/usr/bin/python

""" the tool that checks if there is a mapping for particular career in mapping JSON which looks like:

"mapping": [
    {
        "exchange": "google",
        "map": [
            {
                "key": "70000",
                "value": "ntt docomo"
            },
            {
                "key": "208-01",
                "value": "orange"
            },
            ....
"""
from __future__ import print_function
import json

mapping_file = '/Users/nkolchenko/mappings/data/carriers.json'
pattern_list = [
'404-01',
'404-04',
'404-05',
'404-07',
'404-09',
'404-11',
'404-12',
'404-13',
'404-14',
'404-15',
'404-18',
'404-19',
'404-20',
'404-22',
'404-24',
'404-27',
'404-30',
'404-34',
'404-36',
'404-38',
'404-43',
'404-44',
'404-46',
'404-50',
'404-51',
'404-52',
'404-53',
'404-54',
'404-56',
'404-57',
'404-58',
'404-59',
'404-60',
'404-62',
'404-64',
'404-66',
'404-67',
'404-71',
'404-72',
'404-73',
'404-74',
'404-75',
'404-76',
'404-77',
'404-78',
'404-79',
'404-80',
'404-81',
'404-82',
'404-83',
'404-84',
'404-85',
'404-86',
'404-87',
'404-88',
'404-89',
'405-01',
'405-03',
'405-04',
'405-05',
'405-06',
'405-07',
'405-08',
'405-09',
'405-10',
'405-11',
'405-12',
'405-13',
'405-14',
'405-15',
'405-17',
'405-18',
'405-19',
'405-20',
'405-21',
'405-22',
'405-23',
'405-66',
'405-67',
'405-70',
'405-750',
'405-751',
'405-752',
'405-753',
'405-754',
'405-755',
'405-756',
'405-799',
'405-840',
'405-845',
'405-846',
'405-847',
'405-848',
'405-849',
'405-850',
'405-851',
'405-852',
'405-853',
'405-854',
'405-855',
'405-856',
'405-857',
'405-858',
'405-859',
'405-860',
'405-861',
'405-862',
'405-863',
'405-864',
'405-865',
'405-866',
'405-867',
'405-868',
'405-869',
'405-870',
'405-871',
'405-872',
'405-873',
'405-874',
'405-908',
'405-909',
'405-910',
'405-911'
]

exch_list = [
    'google',
    'axonix',
    'smartrtb',
    'opera',
    'smaato',
    'pubmatic',
    'mopub',
    'nexage',
    'rubicon',
    'GENERIC'
]

with open(mapping_file) as mappings_file:
    data = json.load(mappings_file)

    mapping = data['mapping']
    i = 0
    count = 0
    while i < len(mapping):
        #   lets process each entity in mapping list
        entity = mapping[i]
        map = entity['map']
        i = i + 1
        n = 0

        if entity['exchange'] in exch_list:
            #       lets get data only for exchanges needed

            s_count = 0
            f_count = len(pattern_list)

            for cmp in pattern_list:
                #print(str(entity['exchange'])+' looking for: '+str(cmp))
                while n < len(map):  # processing each element of 'map'
                    element = map[n]
                    #for cmp in pattern_list:
                    if element['key'] == cmp :
                        #print('got '+str(cmp)+' for exch: '+str(entity['exchange']))
                        s_count = s_count + 1
                        f_count = f_count -1
                    n = n + 1
                n=0


            if s_count != 0:
                #print(str(entity['exchange']) + ' contains '+str(len(pattern_list))+' patterns. '
                print(str(entity['exchange']) + ' : ' 
                      + str(s_count) + ' patterns are there and '+str(f_count)+' are missed ')
            else:
                print(str(entity['exchange']))