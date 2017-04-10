'''This is going to be the main file'''
import configparser
import logging
from logging.handlers import TimedRotatingFileHandler


def create_timed_rotating_log(path):
    logger = logging.getLogger("BasicLogger")

    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(path,
            when="m",
            interval=1,
            backupCount=5)
    logger.addHandler(handler)


    logger.info("wow created a logger")

def main():
    log_file = "main_log.log"
    create_timed_rotating_log("log/" + log_file)
    logger = logging.getLogger("BasicLogger")
    logger.info("hello from main")
    config = configparser.ConfigParser()
    config.read('config.ini')

    # How to use the config values. REMOVE when done with setup of this!
    print(config.sections())
    print('scale of this whole thing from config file is: ' + config['grid']['scale'])
    # To get the values as integers:
    i = int(config['grid']['max_position_z'])
    print(i+2)

if __name__ == "__main__":
    main()
