#!/usr/bin/env python3

import sys
import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-i','--ipaddress',dest='varString', type=str,default='205.251.250.0', help='ip address of host')

args = parser.parse_args()
print((parser.parse_args()).varString)


url = f"http://ipinfo.io/205.251.250.0/json"

jsonResp = requests.get(url)

dictResp = json.loads(jsonResp.text)

for key in dictResp.keys():
    print(f"{key: <10}:{dictResp[key]: <10}")
