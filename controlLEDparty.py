import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

ControlPin = [29,31,33,35]

for pin in ControlPin:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)

def vorwaerts(schritte):
	seq_vorwaerts = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
	for number in range(schritte)
		for row in range(4):
			for columns in range(4):
				GPIO.output(ControlPin[columns],seq[row][columns])
				time.sleep(1)

def rueckwaerts(schritte):
	seq_rueckwaerts = [[0,0,0,1], [0,0,1,0], [0,1,0,0], [1,0,0,0]]
	for number in range(schritte)
		for row in range(4):
			for columns in range(4):
				GPIO.output(ControlPin[columns],seq[row][columns])
				time.sleep(1)


def main():
schritte = input("Wie weit willst du laufen?: ")
if schritte >= 1
	vorwaerts(schritte)
	print('vorwärts um', schritte)
elif schritte <= -1
	rueckwaerts(schritte)
	print('rückwärts um' schritte)
else
	print('Dann bleib ich stehen')




GPIO.cleanup()
