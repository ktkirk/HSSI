from __future__ import print_function
import sys, signal, atexit
import json

__author__ = 'KT Kirk'
__all__ = ['keys', 'atexit', 'signal']

## Exit handlers ##
# This function stops python from printing a stacktrace when you hit control-C
def SIGINTHandler(signum, frame):
    raise SystemExit

# This function lets you run code on exit, including functions from myUVSensor
def exitHandler():
    print("Exiting")
    try:
        sys.exit(0)
    except KeyError:
        pass

# Register exit handlers
atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)


# Load data.sparkfun.com keys file
with open("keys_n1YRX98dq9C6X0LrZdvD.json") as json_file:
    keys = json.load(json_file)