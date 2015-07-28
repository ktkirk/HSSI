
from __future__ import print_function
import requests
import socket
import base64
import time

KEY = socket.gethostname()
URL = "http://10.232.106.230:8500/v1/kv/" + KEY

data = 'Hello ' + KEY

# Put data on consul server
put = requests.put(URL, data)

time.sleep(.5)

# Get data from consul server
get = requests.get(URL)

# Output status code and data type
print(get, type(get.json()))
d = get.json()[0]
print(d)

# Decode value data from base64
print(base64.b64decode(d['Value']))

