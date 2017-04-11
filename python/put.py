#!/usr/bin/python

# auth on api.strikead.com. Requires json in format:
#  { "email": "nobodyone@example.com", "password": "ololo"}

import requests
import json

fusion_base = 'https://api.strikead.com/v1.1'

with open('/Users/nkolchenko/fusion-api/sign_in.json', 'r') as json_file:
    data = json.load(json_file)

try:
    auth = requests.post('{0}/login'.format(fusion_base), json=data)
    auth.raise_for_status()
    silex = auth.json()['token']
except (requests.HTTPError, KeyError):
    print('Failed to authorise')


campaign_ids = [
    6882
    ]


for campaign_id in campaign_ids:
    try:
        headers = {'Accept': 'application/json', 'X-Authorization': silex}
        r = requests.get('{0}/campaigns/{1}'.format(fusion_base, campaign_id), headers=headers)  # XXX:
        r.raise_for_status()

        camp_data = r.json()

        print("Got: "+str(camp_data['line_items']))

            # --------------------------------------

        print(r.status_code)
        print(r.text)

    except ValueError:
        print('FAILED TO PROCESS CREATIVE_ID {0}: response is invalid JSON'.format(campaign_id))
