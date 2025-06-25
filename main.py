import time
import lcd


def main():
    # モーション反応待ち
    # Webカメラ撮影
    # 一致で分岐
    # LCD
    # Buzzer
    # API Request

    # This is test.
    indicator = lcd.Lcd(0x27)
    indicator.print_detecting()
    time.sleep(2)
    indicator.print_approved()
    time.sleep(2)
    indicator.print_rejected()
    time.sleep(2)
    indicator.print_error()
    time.sleep(2)

    try:
        indicator.print_waiting()
        time.sleep(0.2)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
