'''This is going to be the main file'''
import configparser
import logging
from logging.handlers import TimedRotatingFileHandler
import subprocess
from file_operator import FileOperator
from motor import Motor

try:
    import RPi.GPIO as GPIO
except ImportError:
    from fake_gpio import FakeGPIO as GPIO

def create_timed_rotating_log(path):
    logger = logging.getLogger("BasicLogger")

    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(path,
            when="m",
            interval=1,
            backupCount=5)
    logger.addHandler(handler)

def main():
    log_file = "main_log.log"
    create_timed_rotating_log("log/" + log_file)
    logger = logging.getLogger("BasicLogger")
    logger.info("----- Starting Logging Session -----")
    config = configparser.ConfigParser()
    config.read('config.ini')

    # How to use the config values. REMOVE when done with setup of this!
    print(config.sections())
    print('scale of this whole thing from config file is: ' + config['grid']['scale'])
    # To get the values as integers:
    i = int(config['grid']['max_position_z'])
    print(i+2)

    # subprocess.call("../gcodepull.sh", shell=True)

    #opens the file named in the varibles file
    length = range(FileOperator.OpenFile()- 3)
    Motor.setup()
    start = 2
    for row in length:
            # for the appropiated length each row is worked through 
            # and the needet steps are sent to the stepper motors
            next_row = row + start
            delta_step = FileOperator.NextMove(next_row)
            corrected_coords = FileOperator.MoveCorrect(delta_step)
            Motor.move(corrected_coords)
            print('finished')
    GPIO.cleanup()

if __name__ == "__main__":
    main()
