"""Test the grid setup"""
from nose.tools import *
from src.grid import *


def test_path_to_target():
    """Should return relative steps needed to reach point"""
    mygrid = Grid(2, 4, 4000, 4000)
    path = mygrid.path_to_target(4, 1)
    assert_equal(path, [2, -3])


def test_time_sequence():
    """Split movement should return array of step, time arrays"""
    mygrid = Grid(2, 4, 4000, 4000)
    steps_in_time = mygrid.time_sequence([345, 99])
    assert_equal(steps_in_time, [[345, 345], [99, 345]])
