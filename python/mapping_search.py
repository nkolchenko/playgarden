#!/usr/bin/python

# the tool that checks if there is a mapping for particular career in mappining JSON
# JSON looks like that.
#{
#    "mapping": [
#        {
#            "exchange": "google",
#            "map": [
#               {
#                    "key": "70000",
#                    "value": "ntt docomo"
#                },
#                {
#                    "key": "208-01",
#                    "value": "orange"
#                },

from __future__ import print_function
import json
from operator import itemgetter
pattern_list=['404-09','404-10']
exch_list=['google','axonix','smartrtb','opera','smaato','pubmatic',
          'mopub','nexage','rubicon','openrtb20','openrtb21','GENERIC']

file='/Users/nkolchenko/mappings/data/carriers.json'

with open(file) as mappings_file:
    data=json.load(mappings_file)

    mapping=data['mapping']
    i=0
    count=0
    while i < len(mapping):
#   lets process each entity in mapping list
        entity=mapping[i]
        map=entity['map']
        i=i+1
        n=0

        if entity['exchange'] in exch_list:
#       lets get data only for exchanges needed

            count=0
            while n<len(map): # processing each element of 'map'
                element=map[n]

                if element['key'] in pattern_list:
                    #print(element)
                    count=count+1
                n = n + 1

            if count != 0:
                print(str(entity['exchange'])+' contains '+str(count)+' patterns out of '+str(len(pattern_list)))
            else:
                print(str(entity['exchange']))







