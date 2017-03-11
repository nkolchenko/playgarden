#!/usr/bin/python

# auth on api.strikead.com. Requires json in format:
#  { "email": "nobodyone@example.com", "password": "ololo"}


import requests
import json

with open('./sign_in.json', "r") as jsonFile:
    data = json.load(jsonFile)

r = requests.post("https://api.strikead.com/v1.1/login", json = data)
print(r.status_code)
print r.json()
silex = r.json()["token"]

print silex
