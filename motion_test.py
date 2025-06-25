import gpiozero
import time

motion = gpiozero.DigitalInputDevice(pin=24, pull_up=False)

try:
    while True:
        if motion.value == 1:
            print("moved")
        else:
            print("not moved")
        time.sleep(1)
except KeyboardInterrupt:
    motion.close()

