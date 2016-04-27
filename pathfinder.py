import RPi.GPIO as GPIO
import time as sleep

time_1 = 0.5
time_2 = 0.25

GPIO.setmode(GPIO.BOARD)
ControlPin = [31,33,35,37]

pinA = 31
pinB = 33
pinC = 35
pinD = 37

x_position = 0

for pin in ControlPin:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)

def step_one():
	GPIO.output(pinA, 1)
	sleep (time_2)
	GPIO.output(pinD, 0)
	GPIO.output(b, 0)
	sleep (time_1)
def step_two():
	GPIO.output(pinB, 1)
	sleep (time_2)
	GPIO.output(pinA, 0)
	GPIO.output(pinC, 0)
	sleep (time_1)
def step_three():
	GPIO.output(c, 1)
	sleep (time_2)
	GPIO.output(pinD, 0)
	GPIO.output(pinB, 0)
	sleep (time_1)
def step_four():
	GPIO.output(pinD, 1)
	sleep (time_2)
	GPIO.output(pinA, 0)
	GPIO.output(pinC, 0)
	sleep (time_1)

def walking_forwards(steps, x_position):
	number = x_position				#TODO: test
	for number in range(steps):
		step_one()
		step_two()
		step_three()
		step_four

def walking_backwards(steps, x_position):
	number = x_position
	for number in range(steps):
		step_four()
		step_three()
		step_two()
		step_one()

def main():
	steps = input("How far do you want to walk?: ")
	if steps >= 1:
		walking_forwards(stpes, x_position)
		print('fowards by', steps)
	elif steps <= -1:
		walking_backwards(steps, x_position)
		print('backwards by' steps)
	else:
		print('Stopped')
