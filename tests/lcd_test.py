import LCD1602
import time
import datetime


def setup():
    LCD1602.init(0x27, 1)


MSG = {
        'detecting': [
            'Face Detecting..',
            '\xb6\xb5 \xc6\xdd\xbc\xae\xb3\xc1\xad\xb3',
            ],
        'approved': [
            '() Approved!',
            '\xc6\xdd\xbc\xae\xb3 \xbe\xb2\xba\xb3',
            ],
        'rejected': [
            '>< Rejected!',
            '\xc6\xdd\xbc\xae\xb3 \xbc\xaf\xca\xdf\xb2!',
            ],
        'error': ['- ERROR! - ', '- \xb4\xd7\xb0 \xca\xaf\xbe\xb2! -'],
        }


try:
    setup()

    LCD1602.clear()
    now = datetime.datetime.now()
    LCD1602.write(0, 0, now.strftime('%Y/%m/%d %H:%M'))
    LCD1602.write(0, 1, 'Waiting motion...')
    time.sleep(2)

    LCD1602.clear()
    LCD1602.write(0, 0, MSG['detecting'][0])
    LCD1602.write(0, 1, MSG['detecting'][1])
    time.sleep(2)

    LCD1602.clear()
    LCD1602.write(0, 0, MSG['approved'][0])
    LCD1602.write(0, 1, MSG['approved'][1])
    time.sleep(2)

    LCD1602.clear()
    LCD1602.write(0, 0, MSG['rejected'][0])
    LCD1602.write(0, 1, MSG['rejected'][1])
    time.sleep(2)

    LCD1602.clear()
    LCD1602.write(0, 0, MSG['error'][0])
    LCD1602.write(0, 1, MSG['error'][1])
    time.sleep(2)

except KeyboardInterrupt:
    pass
