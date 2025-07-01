import gpiozero


class MotionSensor:
    def __init__(self, gpio_pin: int):
        self.sensor = gpiozero.DigitalInputDevice(pin=gpio_pin, pull_up=False)

    def get_is_moved(self) -> bool:
        return self.sensor.value == 1

    def close(self):
        self.sensor.close()
