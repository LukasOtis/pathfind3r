"""Logic for working through sequences of steps."""
from grid import *
from sequence import *
import time

class MotorController:
    """MotorController."""

    def __init__(self, sequence, motor, position):
        """Init."""
        self.sequence = sequence
        self.motor = motor
        self.position = position
        self.sleep_time = 0.01

    def motor_sleep(self):
        time.sleep(self.sleep_time)

    def move(self, pattern):
        
