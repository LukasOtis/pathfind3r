"""Test the g-code parser"""
from nose.tools import *
from src.gcodeparser import *


def test_fromLine_coords():
    """Should return a GCodeParser Object with x,y,z"""
    line = "G01 X0 Y20 Z1"
    subject = GCodeParser.fromLine(line)
    assert_equal(subject.ycoord, 20)
    assert_equal(subject.xcoord, 0)
    assert_equal(subject.zcoord, 1)

def test_not_set_axis():
    """Should still return a valid object if one axis is not mentioned"""
    line = "G01 X123123 Z0"
    subject = GCodeParser.fromLine(line)
    assert_equal(subject.xcoord, 123123)
    assert_equal(subject.ycoord, 0)
