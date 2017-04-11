from test_operator import FileOperator
from test_motor import Motor

length = range(FileOperator.OpenFile()- 3)
start = 2
for row in length:
	next_row = row + start
	delta_step = FileOperator.NextMove(next_row)
	corrected_coords = FileOperator.MoveCorrect(delta_step)
	Motor.move(corrected_coords)