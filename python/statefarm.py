#!/usr/bin/python
import json
import urllib2
import re
import requests

silex = 'silex_******' # obtain silex beforehand

collection = [
#array of campaign ids
]

manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
handler = urllib2.HTTPBasicAuthHandler(manager)

director = urllib2.OpenerDirector()
director.add_handler(handler)

# TODO: get rid of 'urllib' and replace it with 'requests'

for creative_id in collection:
    try:
        req = urllib2.Request('https://api.strikead.com/v1.1/creatives/'+str(creative_id), headers = {'X-Authorization' : silex })

        res = urllib2.urlopen(req)
        body= res.read()

        creative_data = json.loads(body)

        #print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


        if (creative_data["type"] == "image"):
            url = creative_data["tracking_code"]

            substr = re.search('HREF=".*"',url)
            substr = substr.group(0)

            tr_code = substr.replace('\"', '')
            tr_code = tr_code.replace('HREF=', '')

            creative_data["tracking_code"] = tr_code

            #print json.dumps(creative_data, sort_keys=True, indent=4, separators=(',', ': '))

            payload = {'Content-Type': 'application/json','X-Authorization' : silex }
            r = requests.put("https://api.strikead.com/v1.1/creatives/"+str(creative_id), json=creative_data, headers=payload)
            print(r.status_code)
            print r.text

    except Exception as e:
        print("FAILED TO PROCESS CREATIVE_ID {0}".format(creative_id))







