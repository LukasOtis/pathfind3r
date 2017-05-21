"""Controls the Motor GPIO movements."""
try:
    import RPi.GPIO as GPIO
except ImportError:
    from fake_gpio import FakeGPIO as GPIO

import time
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

# set config values
# TODO: create __init__ function for motor and move config read to main method
x_motor_direction = int(config['motor_x']['direction_pin'])
x_motor_step = int(config['motor_x']['step_pin'])
y_motor_direction = int(config['motor_y']['direction_pin'])
y_motor_step = int(config['motor_y']['step_pin'])
z_motor_direction = int(config['motor_z']['direction_pin'])
z_motor_step = int(config['motor_z']['step_pin'])
enable_motor_control = int(config['motor_enable']['pin'])
sleep_time = float(config['motor_enable']['sleep'])


class Motor():

    def setup():
        # configure RPI-GPIO
        GPIO.setmode(GPIO.BOARD)
        # set motor_controll pin
        GPIO.setup(enable_motor_control, GPIO.OUT)
        GPIO.output(enable_motor_control, 0)
        # set X Axis Pins
        GPIO.setup(x_motor_direction, GPIO.OUT)
        GPIO.output(x_motor_direction, 0)
        GPIO.setup(x_motor_step, GPIO.OUT)
        GPIO.output(x_motor_step, 0)
        # set y Axis Pins
        GPIO.setup(y_motor_direction, GPIO.OUT)
        GPIO.output(y_motor_direction, 0)
        GPIO.setup(y_motor_step, GPIO.OUT)
        GPIO.output(y_motor_step, 0)
        # set z Axis Pins
        GPIO.setup(z_motor_direction, GPIO.OUT)
        GPIO.output(z_motor_direction, 0)
        GPIO.setup(z_motor_step, GPIO.OUT)
        GPIO.output(z_motor_step, 0)

    def move(next_row):
        #z_movements
        z_steps = next_row[2]
        if z_steps > 0:
            GPIO.output(z_motor_direction, 0)
            for steps in range(z_steps):
                GPIO.output(z_motor_step, 1)
                time.sleep(sleep_time)
                GPIO.output(z_motor_step, 0)
        if z_steps < 0:
            z_steps = z_steps * (-1)
            GPIO.output(z_motor_direction, 1)
            for steps in range(z_steps):
                GPIO.output(z_motor_step, 1)
                time.sleep(sleep_time)
                GPIO.output(z_motor_step, 0)
        #x_movements
        x_steps = next_row[0]
        if x_steps > 0:
            GPIO.output(x_motor_direction, 0)
            for steps in range(x_steps):
                GPIO.output(x_motor_step, 1)
                time.sleep(sleep_time)
                GPIO.output(x_motor_step, 0)
        if x_steps < 0:
            x_steps = x_steps * (-1)
            GPIO.output(x_motor_direction, 1)
            for steps in range(x_steps):
                GPIO.output(x_motor_step, 1)
                time.sleep(sleep_time)
                GPIO.output(x_motor_step, 0)
        #y_movements
        y_steps = next_row[1]
        if y_steps > 0:
            GPIO.output(y_motor_direction, 0)
            for steps in range(y_steps):
                GPIO.output(y_motor_step, 1)
                time.sleep(sleep_time)
                GPIO.output(y_motor_step, 0)
        if y_steps < 0:
            y_steps = y_steps * (-1)
            GPIO.output(y_motor_direction, 1)
            for steps in range(y_steps):
                GPIO.output(y_motor_step, 1)
                time.sleep(sleep_time)
                GPIO.output(y_motor_step, 0)
