
from __future__ import print_function
from pprint import pprint
import requests
import socket
import base64
import time

KEY = socket.gethostname()
URL = "http://10.232.106.230:8500/v1/kv/" + KEY

put_data = 'Hello ' + KEY

# Put data on consul server
put = requests.put(URL, put_data)
print("Put Data: {}".format(put_data), put)
print()

time.sleep(.5)

# Get data from consul server
get = requests.get(URL)

# Output status code and data type
#print(get, type(get.json()))
print()
d = get.json()[0]
pprint(d)
print()

# Decode value data from base64
get_data = base64.b64decode(d['Value']).decode()
print("Get Data: {}".format(get_data), get)

