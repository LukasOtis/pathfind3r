'''This is going to be the main file'''
import logging
import time
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
    # for i in range(6):
    #     logger.info("This is a test!")
    #     time.sleep(75)

def main():
    log_file = "main_log.log"
    create_timed_rotating_log("log/" + log_file)
    logger = logging.getLogger("BasicLogger")
    logger.info("hello from main")

if __name__ == "__main__":
    main()
