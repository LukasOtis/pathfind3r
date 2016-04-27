from nose.tools import *
from src.pathfinder import *

def test_is_stepper_counting():
    assert_equal(move(0, 0, 0), 'nothing changed')
