# import RPi.GPIO as GPIO
from test.devStubs import *
import time as sleep

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


# base rotation functions for stepping motors
def step_one():
    GPIO.output(pinA, 1)
    sleep(time_2)
    GPIO.output(pinD, 0)
    GPIO.output(pinB, 0)
    sleep(time_1)


def step_two():
    GPIO.output(pinB, 1)
    sleep(time_2)
    GPIO.output(pinA, 0)
    GPIO.output(pinC, 0)
    sleep(time_1)


def step_three():
    GPIO.output(pinC, 1)
    sleep(time_2)
    GPIO.output(pinD, 0)
    GPIO.output(pinB, 0)
    sleep(time_1)


def step_four():
    GPIO.output(pinD, 1)
    sleep(time_2)
    GPIO.output(pinA, 0)
    GPIO.output(pinC, 0)
    sleep(time_1)


# define coordinate system
horizontal_max_value = 0
horizontal_min_value = -horizontal_max_value

# create start state
x_position = 0
rotation_position = 0


def move(steps):
    if(steps == 0):
        print('nothing changed')

    boundsFlag = x_position + steps
    if(boundsFlag > horizontal_max_value | boundsFlag < horizontal_min_value):
        print('error: command out of bounds')
    if(steps < 0):
        rotate_backwards(steps)
    else:
        rotate_forwards(steps)


# move forward a given amount of quarters
def rotate_forwards(steps):
    for step in steps:
        if (rotation_position == 1):
            step_two
            rotation_position = 2
            x_position = x_position + 1

        if (rotation_position == 2):
            step_three
            rotation_position = 3
            x_position = x_position + 1

        if (rotation_position == 3):
            step_four
            rotation_position = 4
            x_position = x_position + 1

        if (rotation_position == 4):
            step_one
            rotation_position = 1
            x_position = x_position + 1


# moe backwards a given amount of quaters
def rotate_backwards(steps):
    for step in steps:
        if (rotation_position == 1):
            step_four
            rotation_position = 4
            x_position = x_position - 1

        if (rotation_position == 2):
            step_one
            rotation_position = 1
            x_position = x_position - 1

        if (rotation_position == 3):
            step_two
            rotation_position = 2
            x_position = x_position - 1

        if (rotation_position == 4):
            step_three
            rotation_position = 3
            x_position = x_position - 1


'''main method'''
def main():
    while(true):
        steps = int(input("How far do you want to walk?: "))
        move(steps)
        print('Done with steps --> New x_position: ' + x_position)
