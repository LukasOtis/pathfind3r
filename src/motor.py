"""Controls the Motor GPIO movements."""
try:
    import RPi.GPIO as GPIO
except ImportError:
    from fake_gpio import FakeGPIO as GPIO


class Motor():
    """Motor."""

    def __init__(self, motor_id, pins, max_position):
        """Initialize."""
        self.motor_id = motor_id
        self.pins = pins
        self.max_position = max_position
        GPIO.setmode(GPIO.BOARD)
        for pin in self.pins:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, 0)

    def out(self, pin, set_to):
        """Helper function to set 0 or 1 to gpio pin."""
        GPIO.output(self.pins[pin - 1], set_to)

    def step_zero(self):
        """Setting gpio pins and sleeping."""
        self.out(1, 1)
        self.out(2, 0)
        self.out(3, 0)
        self.out(4, 0)

    def step_one(self):
        """Setting gpio pins and sleeping."""
        self.out(1, 1)
        self.out(3, 1)
        self.out(2, 0)
        self.out(4, 0)

    def step_two(self):
        """Setting gpio pins and sleeping."""
        self.out(3, 1)
        self.out(2, 0)
        self.out(1, 0)
        self.out(4, 0)

    def step_three(self):
        """Setting gpio pins and sleeping."""
        self.out(3, 1)
        self.out(2, 1)
        self.out(1, 0)
        self.out(4, 0)

    def step_four(self):
        """Setting gpio pins and sleeping."""
        self.out(2, 1)
        self.out(1, 0)
        self.out(4, 0)
        self.out(3, 0)

    def step_five(self):
        """Setting gpio pins and sleeping."""
        self.out(2, 1)
        self.out(4, 1)
        self.out(1, 0)
        self.out(3, 0)

    def step_six(self):
        """Setting gpio pins and sleeping."""
        self.out(4, 1)
        self.out(1, 0)
        self.out(2, 0)
        self.out(3, 0)

    def step_seven(self):
        """Setting gpio pins and sleeping."""
        self.out(4, 1)
        self.out(1, 1)
        self.out(2, 0)
        self.out(3, 0)
