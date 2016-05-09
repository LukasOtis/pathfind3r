""""""
from time import sleep


class GpioMockController():
    """one instance corresponses to one motor"""

    def __init__(self, sleepTime):
        self.sleepTime = sleepTime

    # base rotation functions for stepping motors
    def step_one(self):
        sleep(self.sleepTime)
    def step_two(self):
        sleep(self.sleepTime)
    def step_three(self):
        sleep(self.sleepTime)
    def step_four(self):
        sleep(self.sleepTime)

    def move(self, steps, x_position):
        """roatates (1 command) and returns the new rotation_position."""
        r_initial = (x_position % 4)
        r_expected = (x_position + steps) % 4
        if(steps == 0):
            return x_position
        if(steps < 0):
            r_return = self.rotate_backwards(steps, r_initial)
            if(r_expected == r_return):
                return x_position + steps
            else:
                raise Exception('internal error with backward rotation')
        else:
            r_return = self.rotate_forwards(steps, r_initial)
            if(r_expected == r_return):
                return x_position + steps
            else:
                raise Exception('internal error with forward rotation')

    def rotate_forwards(self, steps, rotation_position):
        """move forward a given amount of quarters."""
        for step in range(steps):
            if (rotation_position == 0):
                self.step_two()

            if (rotation_position == 1):
                self.step_three()

            if (rotation_position == 2):
                self.step_four()

            if (rotation_position == 3):
                self.step_one()

            rotation_position += 1

            if rotation_position == 4:
                rotation_position = 0

        return(rotation_position)

    def rotate_backwards(self, steps, rotation_position):
        """move backward a given amount of quarters."""
        for step in range(steps * (-1)):
            if (rotation_position == 0):
                self.step_four

            if (rotation_position == 1):
                self.step_one

            if (rotation_position == 2):
                self.step_two

            if (rotation_position == 3):
                self.step_three

            rotation_position -= 1

            if rotation_position == -1:
                rotation_position = 3

        return(rotation_position)
