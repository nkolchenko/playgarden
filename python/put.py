#!/usr/bin/python
import requests
import json
import urllib2
import re

#payload = {'X-Authorization' : 'silex_58bd616ef2ff9'}
#with open('./sign_in.json', "r") as jsonFile:
 #   data = json.load(jsonFile)

#r = requests.get("https://api.strikead.com/v1.1/creatives/416920", headers = {'X-Authorization' : 'silex_58bede41f0271'})
#print(r.status_code)
#print r.text


####
#collection = [413223,413224,413225]

#manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
#handler = urllib2.HTTPBasicAuthHandler(manager)

#director = urllib2.OpenerDirector()
#director.add_handler(handler)

#for x in collection:
#    req = requests.get('https://api.strikead.com/v1.1/creatives/'+str(x), headers = {'X-Authorization' : 'silex_58bede41f0271'})

#    creative_data = json.loads(req)
#    print json.dumps(creative_data, sort_keys=True, indent=4, separators=(',', ': '))
