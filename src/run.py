env_chosen = False
while not env_chosen:
  environment = input('Chose your environment: (r)asberry / (t)est:   ')
  if environment == 'r':
    env_chosen = True
    import RPi.GPIO as GPIO
    from GpioController import *
  elif environment == 't':
    env_chosen = True
    from GpioMockController import *
  else:
    print('please enter r or t as option')

from SequenceController import *
from Motor import *
from Sequence import *

if environment == 'r':
  gpioController = 'something'
elif environment == 't':
  gpioController = GpioMockController(1)
else:
  raise Exception('no real environment set')

sequence = Sequence()
motor = Motor('xMotor', [12,13,14,15], 120)
controller = SequenceController(sequence, motor, 0, gpioController)
sequence_ready = False
print('Ok, great. Next we will define a movement sequence made up of commands')

while not sequence_ready:
  command = input('Enter a command ( the amount of steps to be taken )')
  controller.sequence.enqueue(int(command))
  print('Queue now is: ', controller.sequence.listAll())
  done_input  = input('Done with input phase? y/n')
  if done_input == 'y':
    sequence_ready = True

print('Starting moving through the sequence')
controller = controller.work_sequence()
print('Done with Sequence')
