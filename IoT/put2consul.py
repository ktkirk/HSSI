from __future__ import print_function
import requests
import socket
import time

KEY = socket.gethostname() + "/time"
URL = "http://10.232.106.230:8500/v1/kv/" + KEY

tlocal = time.localtime()

while True:
    put_data = '{}'.format(time.asctime(tlocal))

    # Put data on consul server
    put = requests.put(URL, put_data)
    print("Time: {}".format(put_data), put)
    time.sleep(1)



