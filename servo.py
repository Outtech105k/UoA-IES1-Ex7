import gpiozero


class Servo:
    def __init__(self, gpio_pin: int, default_deg: int = 0):
        self.servo = gpiozero.AngularServo(
            pin=gpio_pin,
            min_pulse_width=0.0005,
            max_pulse_width=0.0024,
            frame_width=0.02,
        )
        self.servo.angle = default_deg

    def set_deg(self, deg: int):
        self.servo.angle = deg

    def close(self):
        self.servo.close()
