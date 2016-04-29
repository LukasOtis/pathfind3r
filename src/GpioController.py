class GpioController():
    """one instance corresponses to one motor"""

    def move(self, steps):
        pass

    # base rotation functions for stepping motors
    def step_one():
        GPIO.output(pinA, 1)
        sleep(time_2)
        GPIO.output(pinD, 0)
        GPIO.output(pinB, 0)
        sleep(time_1)
        print('done with step one')

    def step_two():
        global time_1
        global time_2
        GPIO.output(pinB, 1)
        sleep(time_2)
        GPIO.output(pinA, 0)
        GPIO.output(pinC, 0)
        sleep(time_1)
        print('done with step two')

    def step_three():
        GPIO.output(pinC, 1)
        sleep(time_2)
        GPIO.output(pinD, 0)
        GPIO.output(pinB, 0)
        sleep(time_1)

    def step_four():
        GPIO.output(pinD, 1)
        sleep(time_2)
        GPIO.output(pinA, 0)
        GPIO.output(pinC, 0)
        sleep(time_1)

    # define coordinate system
    horizontal_max_value = 0
    horizontal_min_value = -horizontal_max_value

    # create start state
    x_position = 0
    rotation_position = 1

    def moves(steps, rotation_position, x_position):
        print('trying to move', steps)
        if(steps == 0):
            print('nothing changed')

        # boundsFlag = x_position + steps
        # if(boundsFlag > horizontal_max_value | boundsFlag < horizontal_min_value):
        #    print('error: command out of bounds')
        if(steps < 0):
            rotate_backwards(steps, rotation_position, x_position)
        else:
            return rotate_forwards(steps, rotation_position, x_position)

    # move forward a given amount of quarters
    def rotate_forwards(steps, rotation_position, x_position):
        print('rotating forwards')
        for step in range(steps):
            print('im at step', step)
            if (rotation_position == 1):
                step_two()
                x_position = x_position + 1

            if (rotation_position == 2):
                step_three()
                x_position = x_position + 1

            if (rotation_position == 3):
                step_four()
                x_position = x_position + 1

            if (rotation_position == 4):
                step_one()
                x_position = x_position + 1

            rotation_position += 1

            if rotation_position == 5:
                rotation_position = 1

        return(rotation_position)

    # move backwards a given amount of quaters
    def rotate_backwards(steps, rotation_position, x_position):
        print('rotate backwards')
        for step in range(steps):
            print('im at step', step)
            if (rotation_position == 1):
                step_four
                rotation_position = 4
                x_position = x_position - 1

            if (rotation_position == 2):
                step_one
                rotation_position = 1
                x_position = x_position - 1

            if (rotation_position == 3):
                step_two
                rotation_position = 2
                x_position = x_position - 1

            if (rotation_position == 4):
                step_three
                rotation_position = 3
                x_position = x_position - 1
