"""Controls the Motor GPIO movements."""
try:
    import RPi.GPIO as GPIO
except ImportError:
    from fake_gpio import FakeGPIO as GPIO


class Motor():
    """Motor."""

    def __init__(self, motor_id, pin_direction, pin_steps, max_position):
        """Initialize."""
        self.motor_id = motor_id
        self.pin_direction = pin_direction
        self.pin_steps = pin_steps
        self.max_position = max_position
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin_direction, GPIO.OUT)
        GPIO.output(self.pin_direction, 0)
        GPIO.setup(self.pin_steps, GPIO.OUT)
        GPIO.output(self.pin_steps, 0)

