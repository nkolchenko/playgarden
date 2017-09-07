#!/usr/bin/python
#SUP-1375

from __future__ import print_function

import os.path
import csv
pair_1='427983,427986,427987,427988'
# clicks - 45719     imps - 45717
pair_2='427989,427990,427991,427992'
# clicks - 45720     imps - 45718
empty=''
csv_file="/Users/nkolchenko/111.csv"
outfile="/Users/nkolchenko/45718.csv"

# "timestamp","ad_id","creative_id","retarget_pid","idfa","idfa_md5","idfa_sha1","device_id_sha1","device_id_md5",
# "platform_id_sha1","platform_id_md5","impressions","clicks"

with open(csv_file, 'r') as data_file:
    reader = csv.DictReader(data_file, delimiter=',', quotechar='"')
    with open(outfile, 'w') as f:
        for row in reader:
            if (row['impressions'] == '1' and row['creative_id'] in pair_2 ):
                # store list of all the possible ids
                my_tuple=(row['idfa'],row['idfa_md5'],row['idfa_sha1'],
                      row['device_id_sha1'],row['device_id_md5'], row['platform_id_sha1'],row['platform_id_md5'])
                # now lets take only non empty values from list
                for s in my_tuple:
                    if s:
                        print(s)
                        f.write(str(s)+'\n')






