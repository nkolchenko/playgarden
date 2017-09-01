#!/usr/bin/python

from __future__ import print_function
import json
from api_strikead_connector import get_auth_token

silex = get_auth_token()
print(silex)

