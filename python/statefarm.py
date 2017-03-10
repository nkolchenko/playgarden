#!/usr/bin/python
import json
import urllib2
import re
import requests

silex = '' # obtain silex beforehand

collection = [ 415019 ]


for creative_id in collection:
    try:
        payload = {'Content-Type': 'application/json','X-Authorization' : silex }
        r = requests.get("https://api.strikead.com/v1.1/creatives/"+str(creative_id), headers=payload)

#        print r.text
#        print r.headers['content-type']
#        print r.json()

        creative_data = r.json()

#        print json.dumps(creative_data, sort_keys=True, indent=4, separators=(',', ': '))

        if (creative_data["type"] == "image"):
            url = creative_data["tracking_code"]

            substr = re.search('SRC=".* BORDER',url)
            substr = substr.group(0)
#            print substr
            tr_code = substr.replace('\"', '')
            tr_code = tr_code.replace('SRC=', '')
            tr_code = tr_code.replace(' BORDER', '')
#            print tr_code

            creative_data["tracking_code"] = tr_code

#            print json.dumps(creative_data, sort_keys=True, indent=4, separators=(',', ': '))

            payload = {'Content-Type': 'application/json','X-Authorization' : silex }
            r = requests.put("https://api.strikead.com/v1.1/creatives/"+str(creative_id), json=creative_data, headers=payload)
            print(r.status_code)
            print r.text

    except Exception as e:
        print("FAILED TO PROCESS CREATIVE_ID {0}".format(creative_id))







