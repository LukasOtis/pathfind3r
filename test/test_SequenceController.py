from nose.tools import *
from src.Sequence import *
from src.Motor import *
from src.SequenceController import *


def test_queue_commands():
    """test the base queue functionality."""
    sequence = Sequence()
    assert_equal(sequence.size(), 0)
    sequence.enqueue(1)
    sequence.enqueue(2)
    sequence.enqueue(3)
    sequence.dequeue()
    assert_equal(sequence.size(), 2)


def test_work_sequence_forwards():
    """test dequeue functionality for single forward command."""
    # setup class instances for motor
    sequence = Sequence()
    gpiocontroller = GpioMockController(1)
    motor = Motor('xMotor', [12, 13, 14, 15], 272)
    controller = SequenceController(sequence, motor, 1, gpiocontroller)

    # put some commmands on queue
    sequence.enqueue(1)

    # let SequenceController work on queue
    controller = controller.work_sequence()

    print("the sequence given back from work_sequence is: ", sequence)
    print("the position stored in controller: ", controller.position)

    # returned sequence should be empty now
    assert_equal(controller.sequence.listAll(), [])
    assert_equal(controller.position, 2)


def test_work_sequence_backwards():
    """test dequeue functionality for single backward command."""
    # setup class instances for motor
    sequence = Sequence()
    gpiocontroller = GpioMockController(1)
    motor = Motor('xMotor', [12, 13, 14, 15], 272)
    controller = SequenceController(sequence, motor, 1, gpiocontroller)

    # put some commmands on queue
    sequence.enqueue(-2)

    # let SequenceController work on queue
    controller = controller.work_sequence()

    print("the position stored in controller: ", controller.position)

    # returned sequence should be empty now
    assert_equal(controller.sequence.listAll(), [])
    assert_equal(controller.position, -1)
