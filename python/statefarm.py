#!/usr/bin/python

import re
import requests

# get token from api server
# auth on api.strikead.com requires json like:
#  { "email": "nobodyone@example.com", "password": "ololo"}

with open('./sign_in.json', "r") as jsonFile:
    data = json.load(jsonFile)

auth = requests.post("https://api.strikead.com/v1.1/login", json = data)
silex = auth.json()["token"]

# TODO: automated retrieval of creative Ids

collection = [
xxxxxxx,
yyyyyyy
]


for creative_id in collection:
    try:
        payload = {'Content-Type': 'application/json','X-Authorization' : silex }
        r = requests.get("https://api.strikead.com/v1.1/creatives/"+str(creative_id), headers=payload)

        creative_data = r.json()

#        print json.dumps(creative_data, sort_keys=True, indent=4, separators=(',', ': '))

        if (creative_data["type"] == "image"):
            url = creative_data["tracking_code"]

            substr = re.search('SRC=".* BORDER',url)  #search for particula pattern in "tracking code"
            substr = substr.group(0)
#            print substr
            tr_code = substr.replace('\"', '')        # don't know how to substitute everything I need;
            tr_code = tr_code.replace('SRC=', '')     # thus there are 3 iterations
            tr_code = tr_code.replace(' BORDER', '')
#            print tr_code

            creative_data["tracking_code"] = tr_code

#            print json.dumps(creative_data, sort_keys=True, indent=4, separators=(',', ': '))

            payload = {'Content-Type': 'application/json','X-Authorization' : silex }
            r = requests.put("https://api.strikead.com/v1.1/creatives/"+str(creative_id),
                             json=creative_data, headers=payload)
            print(r.status_code)
            print r.text

    except Exception as e:
        print("FAILED TO PROCESS CREATIVE_ID {0}".format(creative_id))







