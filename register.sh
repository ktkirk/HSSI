#!/bin/bash

NODE=${1-$(hostname -s)}
CONSUL_URL="http://10.232.106.230:8500/v1/catalog/register"
WIFI_IP=$(ip addr show dev wlan0 | awk '/inet / { split($2, ip, "/"); print ip[1] }')

DATA="$(printf '{"Datacenter": "hssi", "Node": "%s", "Address": "%s"}' ${NODE} ${WIFI_IP})"

set -x 
#echo "$DATA"
curl -X PUT -d "${DATA}" $CONSUL_URL

