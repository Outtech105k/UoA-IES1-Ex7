
import gpiozero
import time


class Buzzer:
    def __init__(self, gpio_pin: int):
        self.buz = gpiozero.DigitalOutputDevice(pin=gpio_pin)

    def sound(self, on_sec=1, off_sec=0):
        self.buz.on()
        time.sleep(on_sec)
        self.buz.off()
        time.sleep(off_sec)

    def sound_wait(self):
        for i in range(3):
            self.sound(0.1, 0.9)
        
    def sound_accept(self):
        self.sound(0.1, 0.3)
        self.sound(0.5)

    def sound_reject(self):
        for i in range(5):
            self.sound(0.1, 0.2)

    def sound_error(self):
        for i in range(3):
            self.sound(0.6, 0.2)
