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

    def rotate_forwards(self, steps, rotation_position):
        """Move forward a given amount of quarters."""

        if rotation_position == 0:
            self.motor.step_one()
            rotation_position += 1
            halt

        elif rotation_position == 1:
            self.motor.step_two()
            rotation_position += 1
            halt

        elif rotation_position == 2:
            self.motor.step_three()
            rotation_position += 1
            halt

        elif rotation_position == 3:
            self.motor.step_four()
            rotation_position += 1
            halt

        elif rotation_position == 4:
            self.motor.step_five()
            rotation_position += 1
            halt

        elif rotation_position == 5:
            self.motor.step_six()
            rotation_position += 1
            halt

        elif rotation_position == 6:
            self.motor.step_seven()
            rotation_position += 1
            halt

        else:
            self.motor.step_zero()
            rotation_position = 0
            halt

        return rotation_position

    def rotate_backwards(self, steps, rotation_position):
        """Move backwards a given amount of quarters."""

        if rotation_position == 0:
            self.motor.step_two()
            rotation_position += 1
            halt

        elif rotation_position == 1:
            self.motor.step_three()
            rotation_position += 1
            halt

        elif rotation_position == 2:
            self.motor.step_four()
            rotation_position += 1
            halt

        elif rotation_position == 3:
            self.motor.step_five()
            rotation_position += 1
            halt

        elif rotation_position == 4:
            self.motor.step_six()
            rotation_position += 1
            halt

        elif rotation_position == 5:
            self.motor.step_seven()
            rotation_position += 1
            halt

        elif rotation_position == 6:
            self.motor.step_eight()
            rotation_position += 1
            halt

        else:
            self.motor.step_one()
            rotation_position = 0
            halt

        return rotation_position

    def rotate_backwards(self, steps, rotation_position):
        """Move backward a given amount of quarters."""
        for step in range(steps * (-1)):

            if rotation_position == 0:
                self.motor.step_four()
                time.sleep(0.01)

            if rotation_position == 1:
                self.motor.step_one()
                time.sleep(0.01)

            if rotation_position == 2:
                self.motor.step_two()
                time.sleep(0.01)

            if rotation_position == 3:
                self.motor.step_three()
                time.sleep(0.01)

            rotation_position -= 1

            if rotation_position == -1:
                rotation_position = 3

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
