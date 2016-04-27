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


def move(steps, x_position, rotation_position):
    if(steps == 0):
        return 'nothing changed'

    boundsFlag = x_position + steps
    if(boundsFlag > horizontal_max_value | boundsFlag < horizontal_min_value):
        return 'error: command out of bounds'
    if(steps < 0):
        rotate_backwards(steps, x_position, rotation_position)
    else:
        rotate_forwards(steps, x_position, rotation_position)


# move forward a given amount of quarters
def rotate_forwards(steps, x_position, rotation_position):
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


# TODO: implement equivalent to rotate_forwards function
def rotate_backwards(steps, x_position):
    number = x_position
    for number in range(steps):
        step_four()
        step_three()
        step_two()
        step_one()


def main():
    steps = input("How far do you want to walk?: ")
    if steps >= 1:
        rotate_forwards(steps, x_position, rotation_position)
        print('fowards by', steps)
    elif steps <= -1:
        rotate_backwards(steps, x_position, rotation_position)
        print('backwards by' + steps)
    else:
        print('Stopped')
