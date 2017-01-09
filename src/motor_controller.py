"""Logic for working through sequences of steps."""
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

    def rotate_forwards(self, rotation_position):
        """Move forward a given amount of quarters."""

        if rotation_position == 0:
            self.motor.step_one()
            rotation_position += 1
            motor_sleep

        elif rotation_position == 1:
            self.motor.step_two()
            rotation_position += 1
            motor_sleep

        elif rotation_position == 2:
            self.motor.step_three()
            rotation_position += 1
            motor_sleep

        elif rotation_position == 3:
            self.motor.step_four()
            rotation_position += 1
            motor_sleep

        elif rotation_position == 4:
            self.motor.step_five()
            rotation_position += 1
            motor_sleep

        elif rotation_position == 5:
            self.motor.step_six()
            rotation_position += 1
            motor_sleep

        elif rotation_position == 6:
            self.motor.step_seven()
            rotation_position += 1
            motor_sleep

        else:
            self.motor.step_zero()
            rotation_position = 0
            motor_sleep

        return rotation_position

    def rotate_backwards(self, rotation_position):
        """Move backwards a given amount of quarters."""

        if rotation_position == 0:
            self.motor.step_seven()
            rotation_position == 7
            motor_sleep

        elif rotation_position == 1:
            self.motor.step_zero()
            rotation_position -= 1
            motor_sleep

        elif rotation_position == 2:
            self.motor.step_one()
            rotation_position -= 1
            motor_sleep

        elif rotation_position == 3:
            self.motor.step_two()
            rotation_position -= 1
            motor_sleep

        elif rotation_position == 4:
            self.motor.step_three()
            rotation_position -= 1
            motor_sleep

        elif rotation_position == 5:
            self.motor.step_four()
            rotation_position -= 1
            motor_sleep

        elif rotation_position == 6:
            self.motor.step_five()
            rotation_position -= 1
            motor_sleep

        else:
            self.motor.step_six()
            rotation_position -=0
            motor_sleep

        return rotation_position

    def move(self, steps, x_position):
        """Roatate (1 command) and returns the new rotation_position."""
        r_initial = (x_position % 4)

        if steps == 0:
            return x_position

        elif steps < 0:
            self.rotate_backwards(steps, r_initial)

        else:
            self.rotate_forwards(steps, r_initial)
