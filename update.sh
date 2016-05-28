#!/bin/bash

cat >> /etc/opkg/base-feeds.conf  << _EOF_
src/gz all http://repo.opkg.net/edison/repo/all
src/gz edison http://repo.opkg.net/edison/repo/edison
src/gz core2-32 http://repo.opkg.net/edison/repo/core2-32
_EOF_

opkg update
opkg list-upgradable

#opkg upgrade