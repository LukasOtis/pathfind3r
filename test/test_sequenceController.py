from nose.tools import *
from src.Sequence import *
from src.SequenceController import *


def test_queue_commands():
    '''test the base queue functionality'''
    sequence = Sequence()
    assert_equal(sequence.size(), 0)
    sequence.enqueue(1)
    sequence.enqueue(2)
    sequence.enqueue(3)
    sequence.dequeue()
    assert_equal(sequence.size(), 2)

def test_work_sequence():
    '''test the dequeue functionality'''
    sequence = Sequence()
    sequence.enqueue(1)
    sequence.enqueue(2)
    sequence.enqueue(3)
    sequence.enqueue(4)
    sequence.enqueue(5)
    controller = SequenceController(sequence)
    sequence = controller.work_sequence()
    print("the sequence given baack from work_sequence is: ", sequence)
    assert_equal(sequence, [])
