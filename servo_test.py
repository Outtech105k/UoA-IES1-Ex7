from gpiozero import AngularServo
import time

servo = AngularServo(
        pin=17,
        min_pulse_width=0.0005,
        max_pulse_width=0.0024,
        frame_width=0.02
        )
time.sleep(1)
servo.angle = 90

try:
    while True:
        print("Press Enter to move servo...")
        input()

        servo.angle = -90
        print("Open action")
        time.sleep(5)
        servo.angle = 90
        print("Done!", end="\n\n")

except KeyboardInterrupt:
    servo.close()

