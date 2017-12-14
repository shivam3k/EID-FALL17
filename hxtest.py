import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

def cleanAndExit():
    print "Cleaning..."
    GPIO.cleanup()
    print "Bye!"
    sys.exit()

hx = HX711(5, 6)
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
def hx_init():
    hx.set_reading_format("LSB", "MSB")
    hx.set_reference_unit(205.885)
    hx.reset()
    hx.tare()


def hx_read():
    hi =  hx.get_weight(50)
    val = int(hi)
    if val < 0:
        hx.tare()
        print("Taking tare again")
    else:
        print (str(val)+" grams")
    

hx_init()

while True:
    try:
        hx_read()

        
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
