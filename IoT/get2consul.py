from __future__ import print_function
import requests
import socket
import base64
import time

KEY = socket.gethostname() + "/time"
URL = "http://10.232.106.230:8500/v1/kv/" + KEY

while True:
    # Get data from consul server
    get = requests.get(URL)

    # JSON data list to Dict
    d = get.json()[0]

    # Decode value data from base64
    get_data = base64.b64decode(d['Value']).decode()
    print("Time: {}".format(get_data), get)
    time.sleep(1)
