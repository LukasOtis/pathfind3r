"""Running Sequence and feeding it to motor."""
from nose.tools import *
from src.sequence import *


def test_queue_commands():
    """Test the base queue functionality."""
    sequence = Sequence()
    assert_equal(sequence.size(), 0)
    sequence.enqueue(1)
    sequence.enqueue(2)
    sequence.enqueue(3)
    sequence.dequeue()
    assert_equal(sequence.size(), 2)
