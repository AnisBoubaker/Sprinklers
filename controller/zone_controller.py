#!/usr/bin/python
import sys, getopt
import RPi.GPIO as GPIO
import time

# Initialise pin mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# init list with pin numbers

pinList = {1:4, 2:22, 3:6, 4:26}

# Setup pins and shuts down all the zones
for key, pin in pinList.items():
    # loop through pins and set mode default state is 'low'
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


# Parse command line arguments
argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv,"hz:s:",["zone=","state="])
except getopt.GetoptError:
    print 'zones.py -z <number> -s <ON|OFF>'
    sys.exit(2)

state = ''
zone = 0

for opt, arg in opts:
    if opt == '-h':
        print 'zones.py -z <number> -s <ON|OFF>'
        sys.exit()
    elif opt in ("-z", "--zone"):
        zone=int(arg)
    elif opt in ("-s", "--state"):
        state=arg

# Error contol: State could be either ON or OFF
if state not in ('ON', 'OFF'):
    print 'zones.py -z <number> -s <ON|OFF>'
    sys.exit(3)

# Error contol: Zone must be between 1..4
if zone<1 or zone>4:
    print 'Invalid zone (1..4)'
    sys.exit(4)


# Activate/Deactivate the selected zone
if state=='ON':
    GPIO.output(pinList[zone], GPIO.HIGH)
else:
    GPIO.output(pinList[zone], GPIO.LOW)

# Reset GPIO settings
#GPIO.cleanup()
