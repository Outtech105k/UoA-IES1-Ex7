import gpiozero
import time

class Buzzer:
    def __init__(self, pin):
        self.buz = gpiozero.DigitalOutputDevice(pin=pin)

    def sound(self, on_sec=1, off_sec=0):
        self.buz.on()
        time.sleep(on_sec)
        self.buz.off()
        time.sleep(off_sec)

buz = Buzzer(7)

buz.sound(0.2, 0.1)
buz.sound(0.8)

