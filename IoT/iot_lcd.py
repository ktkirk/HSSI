#!/usr/bin/env python

from __future__ import print_function
import time, sys, signal, atexit
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_th02 as th02
import pyupm_guvas12d as upmUV
import pyupm_grovemoisture as upmMoisture
from phant import Phant
import json

__author__ = 'ktkirk'


# Load data.sparkfun.com keys file
with open("keys_n1YRX98dq9C6X0LrZdvD.json") as json_file:
    keys = json.load(json_file)

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
myLcd.setColor(53, 39, 249)
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

## Exit handlers ##
# This function stops python from printing a stacktrace when you hit control-C
def SIGINTHandler(signum, frame):
    raise SystemExit

# This function lets you run code on exit, including functions from myUVSensor
def exitHandler():
    print("Exiting")
    sys.exit(0)

# Register exit handlers
atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)

#
p = Phant(keys["publicKey"],
          'device', 'temp', 'humidity', 'light', "uv", "moisture",
          private_key=keys["privateKey"])

device = open("/factory/serial_number").read().strip('\n')

while(True):
    temp = i2c_th.getTemperature()
    humid = i2c_th.getHumidity()
    lux_val = light.value()
    uv_val = uv.value(GUVAS12D_AREF, SAMPLES_PER_QUERY)
    moisture_val = moisture.value()

    #print("LOG:", device, temp, humid, lux_val, uv_val, moisture_val)
    p.log(device, temp, humid, lux_val, uv_val, moisture_val)
    #print(p.remaining_bytes, p.cap)

    myLcd.setCursor(1, 0)
    myLcd.write("Bytes: {}".format(p.remaining_bytes))

    #data = p.get()
    #print(data['temp'])
    time.sleep(60 * 5)
