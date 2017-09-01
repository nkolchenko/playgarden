#!/usr/bin/python

from __future__ import print_function
import json
import requests
from api_strikead_connector import get_auth_token

fusion_base = 'https://api.strikead.com/v1.1'

silex = get_auth_token()
print(silex)

campaign_ids = [
#    6882
]

for campaign_id in campaign_ids:

    try:
        headers = {'Accept': 'application/json', 'X-Authorization': silex}
        r = requests.get('{0}/campaigns/{1}'.format(fusion_base, campaign_id), headers=headers)  # XXX:
        r.raise_for_status()
        camp_data = r.json()

        print(str(campaign_id)+" status: "+str(r.status_code))
        #print(r.text)

    except ValueError:
        print('FAILED TO PROCESS CAMPAIGN_ID {0}: response is invalid JSON'.format(campaign_id))

    line_item_params = camp_data["line_items"]  # it's a comma separated list of all the line items with their settings
#    targetings = line_items_params[0]

    for line_item in line_item_params:
        #print(line_item["id"])
        li_settings = line_item["targeting"]

        my_check = li_settings.get('inventory_type', "empty")  # checks is inventory_type exists
        if my_check == "empty":
            print(str(line_item["id"])+" has no inventory_type set.")
            # here we should ADD missed targeting
            li_settings['inventory_type']=[u"mobile_web"]

        else:
            if li_settings['inventory_type'] != [u"mobile_web"]:
                print("GOT IT! " + str(line_item["id"]) + " is " + str(li_settings['inventory_type']))
            # here we need to replace any content with mobile_web only
                li_settings['inventory_type'] = [u"mobile_web"]
                print(str(line_item["id"])+" was set to " + str(li_settings['inventory_type']))

    print(camp_data)

# and lets push the resulted JSON back to API.
    r = requests.put('{0}/campaigns/{1}'.format(fusion_base, campaign_id),
                     json=camp_data, headers=headers)  # XXX
    r.raise_for_status()
    print(r.status_code)

