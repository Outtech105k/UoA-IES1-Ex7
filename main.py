import time
import servo


def main():
    # モーション反応待ち
    # Webカメラ撮影
    # 一致で分岐
    # LCD
    # Buzzer
    # API Request

    # This is test.
    srv = servo.Servo(17, 90)
    try:
        while True:
            print("Press Enter to move servo...")
            input()

            srv.set_deg(-90)
            print("Open action")
            time.sleep(5)
            srv.set_deg(90)
            print("Done!", end="\n\n")
    except KeyboardInterrupt:
        srv.close()


if __name__ == '__main__':
    main()
