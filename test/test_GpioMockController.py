from nose.tools import *
from src.Sequence import *
from src.Motor import *
from src.SequenceController import *
from src.GpioMockController import *


def test_moving_along_axis():
    """test adding steps onto position on axis."""
    # setup class instances for motor
    gpioController = GpioMockController(2)
    new_position = gpioController.move(2, 120)
    assert_equal(new_position, 122)
