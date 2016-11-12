"""Represent coordinate system for 2d motor control"""


class Grid():
    """Grid with x and y axis."""

    def __init__(self, x, y, x_max, y_max):
        """Initialize."""
        self.x = x
        self.y = y
        self.x_max = x_max
        self.y_max = y_max

    def valid_target(self, target_x, target_y):
        """Checks if target coordinate is out of bounds"""
        if (target_x > self.x_max or target_y > self.y_max):
            return False
        else:
            return True

    def path_to_target(self, target_x, target_y):
        """Relative steps needed to move from current to target position"""
        return [target_x - self.x, target_y - self.y]

    def time_sequence(self, path):
        """Sets the time the motor has for a given x,y movement"""
        x_steps = path[0]
        y_steps = path[1]
        time = 0
        if (x_steps > y_steps):
            time = x_steps
        else:
            time = y_steps
        return [[x_steps, time], [y_steps, time]]

    def do_steps_in_time(steps, time):
        """Performs steps in given time"""
        ratio = round(time / steps)
        for t in time:
            if t % ratio == 0:
                print("doing step")
            else:
                print("doing nothing")
