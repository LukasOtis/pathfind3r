"""logic for working through sequences of steps."""

from Sequence import *
# from GpioController import *
from GpioMockController import *


class SequenceController(object):
    """SequenceController."""

    def __init__(self, sequence, motor, position, gpiocontroller):
        self.sequence = sequence
        self.motor = motor
        self.position = position
        self.gpiocontroller = gpiocontroller

    def work_sequence(self):
        '''works through all the commmands in the given sequence.'''
        while self.sequence.size() != 0:
            poppedCommand = self.sequence.dequeue()
            print("command to do: ", poppedCommand)
            print("motor max position " , self.motor.maxPosition)
            if (self.position + poppedCommand) > self.motor.maxPosition:
                raise Exception('command oversteps maximal rotation bound')
            if (self.position + poppedCommand) * (-1) > self.motor.maxPosition:
                raise Exception('command oversteps maximal rotation bound')
            # calling the GpioController to handle output to motor
            self.gpiocontroller.move(poppedCommand, self.position)
            # calcutlate the new position
            self.position += poppedCommand

        return self

    def back_to_start(self):
        '''returns to a roation position of 0'''
        # emptying the sequence
        self.sequence.isEmpty()
        # queue the distance to 0 position
        self.sequence.enqueue((self.position) * (-1))
        self.work_sequence()
        return self

