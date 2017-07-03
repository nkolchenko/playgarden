#!/usr/bin/python

# the tool that checks if there is a mapping for particular career in mappining JSON
# JSON looks like that.
#{
#    "description": "Mobile Carriers",
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
pattern='404-09'

file='/Users/nkolchenko/mappings/data/carriers.json'

with open(file) as mappings_file:
    data=json.load(mappings_file)

    mapping=data['mapping']
    i=0
    count=0
    while i < len(mapping):
        section=mapping[i]
        map=section['map']
        #print(str(section['exchange'])+' has '+str(len(map))+' entries')
        i=i+1
        n=0
        while n<len(map):
            element=map[n]
            n=n+1

            if element['key'] == pattern:
                #print(section['exchange'])
                #print(element)
                count=count+1
    print('pattern '+str(pattern)+ ' is found for '+str(count)+' exchanges')





