import	PRi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

ControlPin = [29,31,33,35]

for i in ControlPin: 
	GPIO.setup(i,GPIO.OUT)
	GPIO.output(i,0)

seq = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

for x in range(4)
	for y in range(4):
			GPIO.output(ControlPin[y],seq[x][y])
		time.sleep(1)


GPIO.cleanup()