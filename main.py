import motion
import time
def main():
    # モーション反応待ち
    # Webカメラ撮影
    # 一致で分岐
    # LCD
    # Buzzer
    # API Request

    # This is test.
    mot = motion.MotionSensor(24)
    try:
        while True:
            print("O" if mot.get_is_moved() else "X")
            time.sleep(1)
    except KeyboardInterrupt:
        mot.close()

if __name__=='__main__':
    main()
