"""Controls the Motor GPIO movements."""
try:
    import RPi.GPIO as GPIO
except ImportError:
    from fake_gpio import FakeGPIO as GPIO

import time


class Motor():
    """Motor."""

    def __init__(self, xdir, xstep, ydir, ystep, zdir, zstep, enable, sleep):
        """Initialize."""
        self.xdir = xdir
        self.xstep = xstep
        self.ydir = ydir
        self.ystep = ystep
        self.zdir = zdir
        self.zstep = zstep
        self.enable = enable
        self.sleep = sleep
        self.setup

    def cleanup(self):
        GPIO.cleanup()

    def setup(self):
        # configure RPI-GPIO
        GPIO.setmode(GPIO.BOARD)
        # set motor_controll pin
        GPIO.setup(self.enable, GPIO.OUT)
        GPIO.output(self.enable, 0)
        # set X Axis Pins
        GPIO.setup(self.xdir, GPIO.OUT)
        GPIO.output(self.xdir, 0)
        GPIO.setup(self.xstep, GPIO.OUT)
        GPIO.output(self.xstep, 0)
        # set y Axis Pins
        GPIO.setup(self.ydir, GPIO.OUT)
        GPIO.output(self.ydir, 0)
        GPIO.setup(self.ystep, GPIO.OUT)
        GPIO.output(self.ystep, 0)
        # set z Axis Pins
        GPIO.setup(self.zdir, GPIO.OUT)
        GPIO.output(self.zdir, 0)
        GPIO.setup(self.zstep, GPIO.OUT)
        GPIO.output(self.zstep, 0)

    def move(self, next_row):
        # z_movements
        z_steps = next_row[2]
        if z_steps > 0:
            GPIO.output(self.zdir, 0)
            for steps in range(z_steps):
                GPIO.output(self.zstep, 1)
                time.sleep(self.sleep)
                GPIO.output(self.zstep, 0)
        if z_steps < 0:
            z_steps = z_steps * (-1)
            GPIO.output(self.zdir, 1)
            for steps in range(z_steps):
                GPIO.output(self.zstep, 1)
                time.sleep(self.sleep)
                GPIO.output(self.zstep, 0)
        # x_movements
        x_steps = next_row[0]
        if x_steps > 0:
            GPIO.output(self.xdir, 0)
            for steps in range(x_steps):
                GPIO.output(self.xstep, 1)
                time.sleep(self.sleep)
                GPIO.output(self.xstep, 0)
        if x_steps < 0:
            x_steps = x_steps * (-1)
            GPIO.output(self.xdir, 1)
            for steps in range(x_steps):
                GPIO.output(self.xstep, 1)
                time.sleep(self.sleep)
                GPIO.output(self.xstep, 0)
        # y_movements
        y_steps = next_row[1]
        if y_steps > 0:
            GPIO.output(self.ydir, 0)
            for steps in range(y_steps):
                GPIO.output(self.ystep, 1)
                time.sleep(self.sleep)
                GPIO.output(self.ystep, 0)
        if y_steps < 0:
            y_steps = y_steps * (-1)
            GPIO.output(self.ydir, 1)
            for steps in range(y_steps):
                GPIO.output(self.ystep, 1)
                time.sleep(self.sleep)
                GPIO.output(self.ystep, 0)
