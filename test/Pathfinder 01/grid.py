"""Represent coordinate system for 3d motor control"""
class Grid():
    """Grid with x and y axis."""

    def __init__(self, x, y, z, x_max, y_max, z_max):
        """Initialize."""
        self.x = x
        self.y = y
        self.z = z
        self.x_max = x_max
        self.y_max = y_max
        self.z_max = z_max

    def valid_target(self, target_x, target_y, target_z):
        """Checks if target coordinate is out of bounds"""
        if (target_x > self.x_max or target_y > self.y_max or target_z > self.z_max):
            return False
        elif target_x < 0 or target_y < 0 or target_z < 0:
            return False
        else:
            return True

    def path_from_target(self, target_x, target_y, target_z):
        """Relative steps needed to move from current to target position"""
        return [target_x - self.x, target_y - self.y, target_z - self.z]

    def x_movement(self, path):
        """Checks if there is only x movement"""
        elif target[0] != 0 & target[1] == 0 :
            return True

    def y_movement(self, path):
        """Checks if there is  only y movement"""
        elif target[0] == 0 & target[1] != 0 :
            return True

    def z_movement(self, path):
        """Checks if there is z movement
         and isolates it"""
        if target[0] == 0 & target[1] == 0 & target[2] != 0:
            return True

    def time_for_steps(self, path):
        """Sets the time the motor has for a given x,y movement"""
        x_steps = path[0]
        y_steps = path[1]
        time = 0
        if (x_steps > y_steps):
            time = x_steps
        else:
            time = y_steps

        return [[x_steps, time], [y_steps, time]]

    def single_step_pattern(self, timed_steps):
        """Breaks down time_for_steps array into single steps for each motor"""
        if timed_steps[0][1] != timed_steps[1][1]:
            raise Exception('Both motors need to operate with the same timing')
        time = timed_steps[0][1]
        pattern = []
        ratio_a = round(time / timed_steps[0][0])
        ratio_b = round(time / timed_steps[1][0])
        for t in range(time):
            if t % ratio_a == 0 and t % ratio_b == 0:
                pattern.append([1, 1])
            elif t % ratio_a == 0:
                pattern.append([1, 0])
            elif t % ratio_b == 0:
                pattern.append([0, 1])
            else:
                pattern.append([0, 0])

        return pattern

    def sequence_to_pattern(self, targets):
        """Takes an array of points, times them, return single step pattern"""
        pattern = []
        if len(targets) == 0:
            raise Exception('Targets invalid: Size of input targets cant be zero')
        for target in targets:
            if len(target) != 3:
                raise Exception('Targets invalid: No three targets provided')
            if not self.valid_target(target[0], target[1], target[2]):
                raise Exception('Target is invalid: out of bounds')

            target_path = self.path_from_target(target)
            if z_movement(target_path):
                pattern.append([0, 0, target_path[2]])

            timed_steps = self.time_for_steps(self.path_from_target(target))
            pattern.append(self.single_step_pattern(timed_steps))

        return pattern
