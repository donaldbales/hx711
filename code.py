# https://github.com/adafruit/Adafruit_CircuitPython_HX711
# pip3 install adafruit-circuitpython-hx711

import time
import board
import digitalio
from adafruit_hx711.hx711 import HX711
from adafruit_hx711.analog_in import AnalogIn

data = digitalio.DigitalInOut(board.D5)
data.direction = digitalio.Direction.INPUT
clock = digitalio.DigitalInPut(board.D6)
clock.direction = digitalio.Direction.OUTPUT

hx711 = HX711(data, clock)
channel_a = AnalogIn(hx711, HX711.CHAN_A_GAIN_128)

plate = 5150 #fixed tare for the balance plate

while True:
    # the 100/108000 comes from NAU7802 documentation to convert to grams?
    mass_grams = round((channel_a.value - plate) * 100/108000, 1)
    print("%.1fg" % (mass_grams))
    time.sleep(1)
