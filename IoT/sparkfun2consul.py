
from __future__ import print_function
import requests
import socket
import base64
import time

KEY = socket.gethostname()
URL = "http://10.232.106.230:8500/v1/kv/" + KEY

SPARKFUN_URL = "https://data.sparkfun.com/output/n1YRX98dq9C6X0LrZdvD.csv?page=1"


data_sparkfun = requests.get(SPARKFUN_URL)

cols = ["device","moisture","humidity","uv","light","temp","timestamp"]

for n, line in enumerate(data_sparkfun.iter_lines()):
    print(n, line)
    if n == 1:
        for c, v in zip(cols, line.split(b',')):
            requests.put(URL + '/{}'.format(c), v)

    requests.put(URL + '/rows/{:03}'.format(n), data=line)



