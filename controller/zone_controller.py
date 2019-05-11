#!/usr/bin/python
import sys, getopt
import RPi.GPIO as GPIO
import time

# Initialise pin mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# init list with pin numbers

pinList = {1:4, 2:22, 3:6, 4:26}
usage_str = 'Usage: zones.py [-h | -z <number> -s <ON|OFF|?>]'


def set_zone(zone_num, state):
    for key, pin in pinList.items():
        # loop through pins and set mode default state is 'low'
        GPIO.output(pin, GPIO.LOW)

    # Activate/Deactivate the selected zone
    if state=='ON':
        GPIO.output(pinList[zone_num], GPIO.HIGH)
    else:
        GPIO.output(pinList[zone_num], GPIO.LOW)

def get_zone(zone_num):
    status = GPIO.input(pinList[zone_num])
    if status:
        return 'On'
    else:
        return 'Off'


# Setup pins and shuts down all the zones
for key, pin in pinList.items():
    # loop through pins and set mode default state is 'low'
    GPIO.setup(pin, GPIO.OUT)

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hz:s:",["zone=","state="])
    except getopt.GetoptError:
        print usage_str
        sys.exit(2)

    state = ''
    zone = 0

    for opt, arg in opts:
        if opt == '-h':
            print usage_str
            sys.exit()
        elif opt in ("-z", "--zone"):
            zone=int(arg)
        elif opt in ("-s", "--state"):
            state=arg

    # Error contol: State could be either ON or OFF
    if state not in ('ON', 'OFF', '?'):
        print usage_str
        sys.exit(3)

    # Error contol: Zone must be between 1..4
    if zone<1 or zone>4:
        print 'Invalid zone (1..4)'
        sys.exit(4)


    if state in ('ON', 'OFF'):
        set_zone(zone, state)
        print 'OK'
    elif state == '?':
        print(get_zone(zone))

    

# If script is called directly
if __name__ == "__main__":
    argv = sys.argv[1:]
    main(argv)
