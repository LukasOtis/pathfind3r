import RPi.GPIO as GPIO
# from test.devStubs import *
from time import sleep
from sequenceController import *

time_1 = 0.5
time_2 = 0.25

GPIO.setmode(GPIO.BOARD)
ControlPin = [31, 33, 35, 37]

for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
    print('Set up the pins.')

pinA = 31
pinB = 33
pinC = 35
pinD = 37
