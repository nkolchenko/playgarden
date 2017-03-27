#!/usr/bin/python

from __future__ import print_function

from bs4 import BeautifulSoup
import json
import re
import requests

fusion_base = 'https://api.strikead.com/v1.1'


def transform_tracking_code(tracking_code):
    match = re.search('SRC=".* BORDER', tracking_code)  # search for particular pattern in "tracking code"
    match = match.group(0)

    tr_code = match.replace('\"', '')  # don't know how to substitute everything I need;
    tr_code = tr_code.replace('SRC=', '')  # thus there are 3 iterations
    tr_code = tr_code.replace(' BORDER', '')

    return tr_code


def transform_tracking_code2(tracking_code):
    try:
        soup = BeautifulSoup(tracking_code, 'html.parser')
        return soup.a['href']
    except (TypeError, KeyError):
        return tracking_code


def main():
    # get token from api server
    # auth on api.strikead.com requires json like:
    #  { "email": "nobodyone@example.com", "password": "ololo"}

    with open('/Users/nkolchenko/fusion-api/sign_in.json', 'r') as json_file:
        data = json.load(json_file)

    try:
        auth = requests.post('{0}/login'.format(fusion_base), json=data)
        auth.raise_for_status()
        silex = auth.json()['token']
    except (requests.HTTPError, KeyError):
        print('Failed to authorise')
        return

    # TODO: automated retrieval of creative Ids

    creative_ids = [
        'xxxxx'
    ]

    for creative_id in creative_ids:
        try:
            headers = {'Accept': 'application/json', 'X-Authorization': silex}
            r = requests.get('{0}/creatives/{1}'.format(fusion_base, creative_id), headers=headers)  # XXX:
            r.raise_for_status()

            creative_data = r.json()

            if creative_data['type'] != 'image':
                continue

            # --------------------------------------

            tracking_code = creative_data['tracking_code']
#            print("Got: "+str(tracking_code))
            creative_data['tracking_code'] = transform_tracking_code2(tracking_code)
            print(str(creative_data['id'])+" transformed to : "+str(creative_data['tracking_code']))
            # --------------------------------------

            r = requests.put('{0}/creatives/{1}'.format(fusion_base, creative_id),
                             json=creative_data, headers=headers)  # XXX
            r.raise_for_status()

            print(r.status_code)
#            print(r.text)

        except ValueError:
            print('FAILED TO PROCESS CREATIVE_ID {0}: response is invalid JSON'.format(creative_id))

        except KeyError:
            print('FAILED TO PROCESS CREATIVE_ID {0}: invalid creative format'.format(creative_id))

        except requests.HTTPError:
            print('FAILED TO PROCESS CREATIVE_ID {0}: error contacting server'.format(creative_id))


if __name__ == '__main__':
    main()
