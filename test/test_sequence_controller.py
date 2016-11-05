"""Running Sequence and feeding it to motor."""
from nose.tools import *
from src.sequence import *
from src.motor import *
from src.sequence_controller import *


def test_work_sequence_forwards():
    """Test dequeue functionality for single forward command."""
    sequence = Sequence()
    motor = Motor('xMotor', [12, 13, 14, 15], 2000)
    sequence.enqueue(4)
    controller = SequenceController(sequence, motor, 1)
    controller = controller.work_sequence()
    assert_equal(controller.sequence.listAll(), [])
    assert_equal(controller.position, 5)


def test_work_sequence_backwards():
    """Test dequeue functionality for single backward command."""
    sequence = Sequence()
    motor = Motor('xMotor', [12, 13, 14, 15], 272)
    controller = SequenceController(sequence, motor, 1)
    sequence.enqueue(-10)
    controller = controller.work_sequence()
    assert_equal(controller.sequence.listAll(), [])
    assert_equal(controller.position, -9)


def test_work_sequence_mixed():
    """Test dequeue functionality for mixed commands."""
    sequence = Sequence()
    motor = Motor('xMotor', [12, 13, 14, 15], 272)
    controller = SequenceController(sequence, motor, 0)
    sequence.enqueue(4)
    sequence.enqueue(-10)
    controller = controller.work_sequence()
    print("the position stored in controller: ", controller.position)
    assert_equal(controller.sequence.listAll(), [])
    assert_equal(controller.position, -6)


@raises(Exception)
def test_out_of_bounds_command():
    """Test that command is rejected if it would be moving out of bounds."""
    sequence = Sequence()
    motor = Motor('xMotor', [12, 13, 14, 15], 5)
    controller = SequenceController(sequence, motor, 0)
    sequence.enqueue(4)
    sequence.enqueue(2)
    controller = controller.work_sequence()


def test_back_to_start():
    """Test back to start function after executing sequence."""
    sequence = Sequence()
    motor = Motor('xMotor', [12, 13, 14, 15], 272)
    controller = SequenceController(sequence, motor, 0)
    sequence.enqueue(4)
    controller = controller.work_sequence()
    controller = controller.back_to_start()
    assert_equal(controller.position, 0)
