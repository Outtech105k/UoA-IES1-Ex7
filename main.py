import time
import threading
import queue

import lcd
import motion
import buzzer
import servo
import webapi
import detect


def main():
    motion_sensor = motion.MotionSensor(24)
    lcd16x2 = lcd.Lcd(0x27)
    buzz = buzzer.Buzzer(7)
    serv = servo.Servo(17, -90)
    api = webapi.WebApi()
    facedct = detect.Detect()

    try:
        while True:
            lcd16x2.print_waiting()

            # モーション反応待ち
            seq_count = 0
            while True:
                if motion_sensor.get_is_moved():
                    seq_count += 1
                    print(seq_count)
                    if seq_count >= 10:  # TODO: More count times
                        break
                else:
                    seq_count = 0
                time.sleep(0.1)

            # Webカメラ撮影 (並行処理)
            lcd16x2.print_detecting()

            result_queue: queue.Queue[bool] = queue.Queue()
            detect_thread = threading.Thread(
                target=facedct.detect_task, args=(result_queue,), daemon=True
            )
            detect_thread.start()
            while detect_thread.is_alive():
                buzz.sound_wait()
            detect_thread.join()
            is_detect_approved = result_queue.get()

            # 顔認証の成功可否で分岐
            if is_detect_approved:
                lcd16x2.print_approved()
                buzz.sound_accept()
                serv.set_deg(90)
                time.sleep(5)  # TODO: 5s -> 20s
                serv.set_deg(-90)
                api.approve_post()
            else:
                lcd16x2.print_rejected()
                buzz.sound_reject()
                api.reject_post()

    except KeyboardInterrupt:
        lcd16x2.clear()
        motion_sensor.close()
        serv.close()


if __name__ == "__main__":
    main()
