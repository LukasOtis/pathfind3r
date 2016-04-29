"""logic for working through sequences of steps"""

from Sequence import *
from GpioController import *

class SequenceController(object):
    """SequenceController"""
    def __init__(self, sequence, motor, position, gpiocontroller):
        self.sequence = sequence
        self.motor = motor
        self.position = position
        self.gpiocontroller = gpiocontroller

    def work_sequence(self):
        '''works through all the commmands in the given sequence'''
        while self.sequence.size() != 0:
            poppedCommand = self.sequence.dequeue()
            print("command to do: ", poppedCommand)
            # calling the GpioController to handle output to motor
            self.gpiocontroller.move(poppedCommand)
            # calcutlate the new position
            self.position += poppedCommand
            print("the new position of ", self.motor, " is ", self.position)
        return self.sequence.listAll()
