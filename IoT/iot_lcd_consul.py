#!/usr/bin/env python
from __future__ import print_function
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_th02 as th02
import pyupm_guvas12d as upmUV
import pyupm_grovemoisture as upmMoisture
import requests
import time
from iot_utils import *

__author__ = 'KT Kirk'

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
myLcd.setColor(53, 249, 39 ) # Green
myLcd.setCursor(0,0)
myLcd.write('IoT')

# Instantiate a Grove Moisture sensor on analog pin A1
moisture = upmMoisture.GroveMoisture(1)

# Create the light sensor object using AI2 pin 2
light = grove.GroveLight(2)

# Instantiate a UV sensor on analog pin A3
uv = upmUV.GUVAS12D(3);
# analog voltage, usually 3.3 or 5.0
GUVAS12D_AREF = 5.0;
SAMPLES_PER_QUERY = 1024;

# Create the temperature sensor object using AIO pin 0
i2c_th = th02.TH02()

# Edison serial number
device = open("/factory/serial_number").read().strip('\n')

# Consul key/value
KEY = "hssi/{}".format(device)
URL = "http://10.232.106.230:8500/v1/kv/" + KEY

items = ["moisture","humidity","uv","light","temp","time"]
tlocal = time.localtime()


while True:
    temp = i2c_th.getTemperature()
    humid = i2c_th.getHumidity()
    lux_val = light.value()
    uv_val = uv.value(GUVAS12D_AREF, SAMPLES_PER_QUERY)
    moisture_val = moisture.value()
    put_data = [moisture_val, humid, uv_val, lux_val, temp, time.asctime(tlocal)]

    myLcd.setCursor(1, 0)
    try:
        for c, v in zip(items, put_data):
            requests.put(URL + '/{}'.format(c), v)
    except requests.exceptions.ConnectionError as e:
        print("Connection error")
        myLcd.setColor(255, 0, 0) # Red
        myLcd.write("Error")
    else:
        myLcd.setColor(53, 39, 249) # Blue
         myLcd.write("OK")

    time.sleep(60)