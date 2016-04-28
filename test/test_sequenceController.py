from nose.tools import *
from src.sequenceController import *


def test_that_command_is_stored_in_sequence():
    command = 5
    assert(storeSequence(command))
