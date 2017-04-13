from operator import FileOperator
from motor import Motor

#opens the file named in the varibles file
length = range(FileOperator.OpenFile()- 3)
start = 2
for row in length:
	# for the appropiated length each row is worked through 
	# and the needet steps are sent to the stepper motors
	next_row = row + start
	delta_step = FileOperator.NextMove(next_row)
	corrected_coords = FileOperator.MoveCorrect(delta_step)
	Motor.move(corrected_coords)