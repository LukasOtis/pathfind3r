"""Logic for working through sequences of steps."""
from sequence import *
import time

class SequenceController:
    """SequenceController."""

    def __init__(self, sequence, motor, position):
        """Init."""
        self.sequence = sequence
        self.motor = motor
        self.position = position

    def work_sequence(self):
        """Work through all the commmands in the given sequence."""
        while self.sequence.size() != 0:

            popped_command = self.sequence.dequeue()
            if (self.position + popped_command) > self.motor.max_position:
                raise Exception('command oversteps maximal rotation bound')

            elif (self.position + popped_command) * (-1) > self.motor.max_position:
                raise Exception('command oversteps maximal rotation bound')

            else:
                self.move(popped_command, self.position)
                self.position += popped_command
        return self

    def back_to_start(self):
        """Return to a roation position of 0."""
        self.sequence.isEmpty()
        self.sequence.enqueue((self.position) * (-1))
        self.work_sequence()
        return self

    def rotate_forwards(self, steps, rotation_position):
        """Move forward a given amount of quarters."""

        for step in range(steps):
            if rotation_position == 0:
                self.motor.step_two()
                time.sleep(0.01)

            if rotation_position == 1:
                self.motor.step_three()
                time.sleep(0.01)

            if rotation_position == 2:
                self.motor.step_four()
                time.sleep(0.01)

            if rotation_position == 3:
                self.motor.step_one()
                time.sleep(0.01)

            rotation_position += 1

            if rotation_position == 4:
                rotation_position = 0
                time.sleep(0.01)

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
        r_expected = (x_position + steps) % 4

        if steps == 0:
            return x_position

        elif steps < 0:

            r_return = self.rotate_backwards(steps, r_initial)

            if r_expected == r_return:
                return x_position + steps

            else:
                print('---------------')
                print(r_expected)
                print(r_return)
                raise Exception('internal error with backward rotation')

        else:
            r_return = self.rotate_forwards(steps, r_initial)

            if r_expected == r_return:
                return x_position + steps

            else:
                raise Exception('internal error with forward rotation')
