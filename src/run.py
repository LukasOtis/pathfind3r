'''setting up the sequence handling and raspberry default state'''

# TODO: create menu of options, call setup

while(True):
    steps = input("How far do you want to walk?: ")
    steps = int(steps)
    response = move(steps, rotation_position, x_position)
    print('Done with steps --> New x_position: ', x_position)
    print('new rotation position', response)
    rotation_position = response
