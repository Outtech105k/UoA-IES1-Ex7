import time
import threading
import random

import lcd
import motion
import buzzer
import servo


def detect_task(thread: threading.Thread):
    # TODO: Implement
    wait_time = random.randrange(30, 100)/10
    print(f'{wait_time}s waiting...')
    time.sleep(wait_time)


def main():
    motion_sensor = motion.MotionSensor(24)
    lcd16x2 = lcd.Lcd(0x27)
    buzz = buzzer.Buzzer(7)
    serv = servo.Servo(17, -90)

    try:
        while True:
            lcd16x2.print_waiting()

            # モーション反応待ち
            seq_count = 0
            while True:
                if motion_sensor.get_is_moved():
                    seq_count += 1
                    print(seq_count)
                    if seq_count >= 10:
                        break
                else:
                    seq_count = 0
                time.sleep(0.1)

            # Webカメラ撮影 (並行処理)
            # TODO: Implement here
            lcd16x2.print_detecting()

            detect_thread = threading.Thread(target=detect_task, daemon=True)
            detect_thread.start()
            while detect_thread.is_alive():
                buzz.sound_wait()
            detect_thread.join()
            is_detect_approved = True

            # 一致で分岐
            if is_detect_approved:
                lcd16x2.print_approved()
                buzz.sound_accept()
                serv.set_deg(90)
                time.sleep(5)
                serv.set_deg(-90)
                # TODO: API request
            else:
                lcd16x2.print_rejected()
                buzz.sound_reject()
                # TODO: API request

    except KeyboardInterrupt:
        lcd16x2.print_error()
        motion_sensor.close()
        serv.close()


if __name__ == '__main__':
    main()
