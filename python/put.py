#!/usr/bin/python

# auth on api.strikead.com. Requires json in format:
#  { "email": "nobodyone@example.com", "password": "ololo"}

import requests
import json

fusion_base = 'https://api.strikead.com/v1.1'

with open('./sign_in.json', 'r') as json_file:
    data = json.load(json_file)

try:
    auth = requests.post('{0}/login'.format(fusion_base), json=data)
    auth.raise_for_status()
    silex = auth.json()['token']
except (requests.HTTPError, KeyError):
    print('Failed to authorise')
    return


