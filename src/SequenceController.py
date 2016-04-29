"""logic for working through sequences of steps"""

from Sequence import *


class SequenceController(object):
    """docstring for SequenceController"""
    def __init__(self, sequence):
        self.sequence = sequence

    def work_sequence(self):
        while self.sequence.size() != 0:
            poppedCommand = self.sequence.dequeue()
            print("command to to: ", poppedCommand)
        return self.sequence.listAll()
