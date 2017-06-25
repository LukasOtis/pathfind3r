# The Pathfinder Project

[https://otispathfinder.wordpress.com/](https://otispathfinder.wordpress.com/)

The idea of the pathfind3r project was to build a CNC Machine that would be a lot cheaper than bought ones. Writing the controlling driver ourselves enabled us to understand a lot more about the difficulties in transforming data and controlling hardware reliably. One of the biggest issues that we still face is the one of parallel, synchronised movement of several motors. So this is a work in progress – for sure.

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
