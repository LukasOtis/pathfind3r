import RPi.GPIO as GPIO
import time as sleep

time_1 = 0.5
time_2 = 0.25

GPIO.setmode(GPIO.BOARD)
ControlPin = [31,33,35,37]

a = 31
b = 33
c = 35
d = 37

x_position = 0

for pin in ControlPin:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)

def step_one():
	GPIO.output(a, 1)
	sleep (time_2)
	GPIO.output(d, 0)
	GPIO.output(b, 0)
	sleep (time_1)
def step_two():
	GPIO.output(b, 1)
	sleep (time_2)
	GPIO.output(a, 0)
	GPIO.output(c, 0)
	sleep (time_1)
def step_three():
	GPIO.output(c, 1)
	sleep (time_2)
	GPIO.output(d, 0)
	GPIO.output(b, 0)
	sleep (time_1)
def step_four():
	GPIO.output(d, 1)
	sleep (time_2)
	GPIO.output(a, 0)
	GPIO.output(c, 0)
	sleep (time_1)	

def walking_vorwards(steps, x_position):
	number = x_position 									#das muss ich noch testen
	for number in range(steps):
		step_one()
		step_two()
		step_three()
		step_four

def walking_backwasrds(steps, x_position):
	number = x_position
	for number in range(steps):
		step_four()
		step_three()
		step_two()
		step_one()

def main():
	steps = input("Wie weit willst du laufen?: ")
	if steps >= 1:
		walking_vorwards(stpes, x_position)
		print('vorwärts um', steps)
	elif steps <= -1:
		walking_backwasrds(steps, x_position)
		print('rückwärts um' steps)
	else:
		print('Dann bleib ich stehen')
