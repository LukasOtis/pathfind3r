#The Pathfinder Project

Python based project to control stepping motors with individual movement sequences.
Being build in a TDD kind of way using [nosetests](http://nose.readthedocs.io/en/latest/testing.html). To use on raspberry you need to switch from GpioMockController to GpioController.

###To get started:

- have to have python3 on your machine
- install the nosetests module: "pip install nose"
- to run test suite just run "nosetests" in terminal

###Terminology

In order of abstraction from the hardware, these are the terms used in the code:

- Rotation: the actual, physical position of the motor. There are four rotation positions the motor can have. They are controlled by the GpioController that sets the Gpio pins.
- Command/Steps: the amount of rotation positions the motor is supposed to move forwards or backwards.
- Sequence: A list of commands. Stores multiple instructions for the motor in a FIFO queue (FIFO: first in first out).
