from nose.tools import *
from src.Sequence import *
from src.Motor import *
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
    # setup class instances for motor
    sequence = Sequence()
    gpiocontroller = GpioController()
    motor = Motor('xMotor', [12, 13, 14, 15], 272)
    controller = SequenceController(sequence, motor, 1, gpiocontroller)

    # put some commmands on queue
    sequence.enqueue(1)
    sequence.enqueue(2)
    sequence.enqueue(3)
    sequence.enqueue(-4)
    sequence.enqueue(5)

    # let SequenceController work on queue
    sequence = controller.work_sequence()

    print("the sequence given baack from work_sequence is: ", sequence)
    # returned sequence should be empty now
    assert_equal(sequence, [])
    assert_equal(controller.position, 8)
