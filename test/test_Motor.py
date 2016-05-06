from nose.tools import *
from src.Motor import *


def test_motor_initialization():
    """test creating motor(s)."""
    xMotor = Motor('xMotor', [1, 2, 3, 4], 300)
    assert_equal(xMotor.motorId, 'xMotor')
    assert_equal(xMotor.pins, [1, 2, 3, 4])
    assert_equal(xMotor.maxPosition, 300)
