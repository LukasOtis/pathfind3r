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

    def z_move(self, pattern):
    """Sould recieve a pattern in Form of [x-mm,y-mm,z-mm] with z !=0"""

    """Multiply moving Parts by steps/mm"""

    """execute z-movements"""

    def x_move(self, pattern):
    """Should recieve a pattern in Form of [x-mm,y-mm,z-mm] with x !=0 """

    """Multiply moving Parts by steps/mm"""

    """execute only x-movements"""

    def y_move(self, pattern):

    """Should recieve a pattern in Form of [x-mm,y-mm,z-mm] with y !=0 """

    """Multiply moving Parts by steps/mm"""

    """execute only y-movements"""

    def x_y_move(self, pattern):

    """Should recieve a pattern in Form of [x-mm,y-mm,z-mm] with x & y !=0 """

    """Multiply moving Parts by steps/mm"""

    """execute x-y movements"""