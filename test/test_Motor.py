"""Test Motor."""
from nose.tools import *
from src.motor import *


def test_motor_initialization():
    """Test creating motor."""
    x_motor = Motor('xMotor', [1, 2, 3, 4], 2000)
    assert_equal(x_motor.motor_id, 'xMotor')
    assert_equal(x_motor.pins, [1, 2, 3, 4])
    assert_equal(x_motor.max_position, 2000)
