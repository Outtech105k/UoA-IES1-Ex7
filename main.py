import lcd
import motion
import buzzer


def main():
    motion_sensor = motion.MotionSensor(24)
    lcd16x2 = lcd.Lcd(0x27)
    buzz = buzzer.Buzzer(7)

    # モーション反応待ち
    seq_count = 0
    while True:
        if motion_sensor.get_is_moved():
            seq_count += 1
            if seq_count >= 10:
                break
        else:
            seq_count = 0

    # Webカメラ撮影
    # TODO: Implement here
    lcd16x2.print_waiting()
    for i in range(5):
        buzz.sound_wait()
    is_detect_approved = True

    # 一致で分岐
    if is_detect_approved:
        lcd16x2.print_approved()
        buzz.sound_accept()
        # TODO: API request
    else:
        lcd16x2.print_rejected()
        buzz.sound_reject()
        # TODO: API request

    motion_sensor.close()


if __name__ == '__main__':
    main()
