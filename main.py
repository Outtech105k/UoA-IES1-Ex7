import time
import buzzer


def main():
    # モーション反応待ち
    # Webカメラ撮影
    # 一致で分岐
    # LCD
    # Buzzer
    # API Request

    # This is test.
    buz = buzzer.Buzzer(7)

    print("Wait")
    buz.sound_wait()
    time.sleep(2)

    print("Accept")
    buz.sound_accept()
    time.sleep(2)

    print("Reject")
    buz.sound_reject()
    time.sleep(2)

    print("Error")
    buz.sound_error()


if __name__ == '__main__':
    main()
