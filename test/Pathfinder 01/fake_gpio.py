#!/usr/bin/python
"""FakeGpio."""


class FakeGPIO(object):
    """Stub the basic Rpi Gpio commands."""

    BCM = True
    BOARD = False
    OUT = True
    IN = False
    HIGH = True
    LOW = False

    def setup(*kwds):
        """Mock Rpi GPIO function."""
        return 0

    def output(*args):
        """Mock Rpi GPIO function."""
        return 0

    def input(*args):
        """Mock Rpi GPIO function."""
        return 0

    def cleanup(*args):
        """Mock Rpi GPIO function."""
        return 0

    def setmode(*args):
        """Mock Rpi GPIO function."""
        return 0
