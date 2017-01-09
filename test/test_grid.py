"""Test the grid setup"""
from nose.tools import *
from src.grid import *


def test_path_to_target():
    """Should return relative steps needed to reach point"""
    grid = Grid(2, 4, 4000, 4000)
    subject = grid.path_to_target(4, 1)
    assert_equal(subject, [2, -3])


def test_time_for_steps():
    """Should return array of step, time arrays"""
    grid = Grid(2, 4, 4000, 4000)
    subject = grid.time_for_steps([345, 99])
    assert_equal(subject, [[345, 345], [99, 345]])


def test_single_step_pattern():
    """Should return array of single step instructions"""
    grid = Grid(1, 1, 40000, 40000)
    subject = grid.single_step_pattern([[2, 4], [4, 4]])
    assert_equal(subject, [[1, 1], [0, 1], [1, 1], [0, 1]])


def test_single_step_pattern_timing():
    """Should raise exception if timing of steps are different"""
    grid = Grid(1, 1, 40000, 40000)
    try:
        grid.single_step_pattern([200, 200], [199, 199])
        assert False
    except Exception:
        assert True

def test_sequence_to_pattern():
    """Should return pattern of single steps for each motor"""
    grid = Grid(1, 1, 40000, 40000)
    subject = grid.sequence_to_pattern([[2, 2], [4, 0]])
    assert_equal(subject, [])
