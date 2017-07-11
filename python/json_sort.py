#!/usr/bin/python

from __future__ import print_function
import json
from operator import itemgetter

file='/Users/nkolchenko/mappings/data/carriers.json'
new_file='/Users/nkolchenko/mappings/data/carriers_NEW.json'

with open(file,'r') as mappings_file:
    data=json.load(mappings_file)

    mapping=data['mapping']
    i=len(mapping)
    print(i)
    num=0

    while num < len(mapping):
        list=mapping[num]
        print(list['exchange'])
        sorted_map = sorted(list['map'], key=itemgetter('key'))
        list['map']=sorted_map
        num =num+1

    o = json.dumps(data)
    print(o)

    with open(new_file, 'w') as mappings_new_file:
        mappings_new_file.write(json.dumps(data,indent=4, sort_keys=True))

#    print(list['exchange'])
#    print(list['map'])
#    sorted_map=sorted(list['map'], key=itemgetter('key'))
#    print(sorted_map)
    #exchange=mapping[1]

    #print(exchange)