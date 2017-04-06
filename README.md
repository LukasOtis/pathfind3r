# The Pathfinder Project


Python based project to control stepping motors with individual movement sequences.
Testing is done with [nosetests](http://nose.readthedocs.io/en/latest/testing.html). 

fake_gpio.py mocks the GPIO lib calls allowing you to run this code both on your machine and on a raspberry pi.

### To get started:


- have to have python on your machine
- install the nosetests module: "pip install nose"
- to run test suite just run "nosetests" in terminal
- have a look at the run.py file to do config/setup. There are plans to extract parts of this to a seperate config file.

### Links:

There is a couple of blogposts explaining e.g. the hardware setup in more detail on [here](http://otispathfinder.wordpress.com)
