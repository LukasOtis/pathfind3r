import RPi.GPIO as GPIO
#from test.devStubs import *
from time import sleep

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
    print('done with step one')

def step_two():
    global time_1
    global time_2    
    GPIO.output(pinB, 1)
    sleep(time_2)
    GPIO.output(pinA, 0)
    GPIO.output(pinC, 0)
    sleep(time_1)
    print('done with step two')

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
rotation_position = 1


def move(steps, rotation_position, x_position):
    print('trying to move', steps)
    if(steps == 0):
        print('nothing changed')

    #boundsFlag = x_position + steps
    #if(boundsFlag > horizontal_max_value | boundsFlag < horizontal_min_value):
    #    print('error: command out of bounds')
    if(steps < 0):
        rotate_backwards(steps, rotation_position, x_position)
    else:
        return rotate_forwards(steps, rotation_position, x_position)
 

# move forward a given amount of quarters
def rotate_forwards(steps, rotation_position, x_position):
    print('rotating forwards')
    for step in range(steps):
        print('i´m at step', step)
        if (rotation_position == 1):
            step_two()
            #rotation_position = rotation_position + 1
            x_position = x_position + 1

        if (rotation_position == 2):
            step_three()
            #rotation_position = rotation_position + 1
            x_position = x_position + 1

        if (rotation_position == 3):
            step_four()
            #rotation_position = rotation_position + 1
            x_position = x_position + 1

        if (rotation_position == 4):
            step_one()
            #rotation_position = rotation_position + 1
            x_position = x_position + 1
        
    
        rotation_position += 1
    
        if rotation_position == 5:
            rotation_position = 1
 
    return(rotation_position)
        

# moe backwards a given amount of quaters
def rotate_backwards(steps, rotation_position, x_position):
    print('rotate backwards')
    for step in range(steps):
        print('i´m at step', step)
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
while(True):
    steps = input("How far do you want to walk?: ")
    steps = int(steps)
    response = move(steps, rotation_position, x_position)
    print('Done with steps --> New x_position: ', x_position)
    print('new rotation position', response)
    rotation_position = response
