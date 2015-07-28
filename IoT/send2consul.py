
from __future__ import print_function
import requests
import base64
import json


URL = "http://10.232.106.230:8500/v1/kv/iot"

data = 'Hello'

put = requests.put(URL, data)

get = requests.get(URL)

print(get, get.json(), type(get.json()))

d = get.json()[0]
print(d)
print(base64.b64decode(d['Value']))

