import LCD1602
# HACK: LCD1602はグローバル変数を使用
import datetime


class Lcd:
    def __init__(self, i2c_address: int):
        LCD1602.init(i2c_address, 1)

    def clear(self):
        LCD1602.clear()

    def print_detecting(self):
        self.clear()
        LCD1602.write(0, 0, 'Face Detecting..')
        LCD1602.write(0, 1, '\xb6\xb5 \xc6\xdd\xbc\xae\xb3\xc1\xad\xb3')

    def print_approved(self):
        self.clear()
        LCD1602.write(0, 0, '() Approved!')
        LCD1602.write(0, 1, '\xc6\xdd\xbc\xae\xb3 \xbe\xb2\xba\xb3')

    def print_rejected(self):
        self.clear()
        LCD1602.write(0, 0, '>< Rejected!')
        LCD1602.write(0, 1, '\xc6\xdd\xbc\xae\xb3 \xbc\xaf\xca\xdf\xb2!')

    def print_error(self):
        self.clear()
        LCD1602.write(0, 0, '- ERROR! -')
        LCD1602.write(0, 1, '- \xb4\xd7\xb0 \xca\xaf\xbe\xb2! -')

    def print_waiting(self):
        self.clear()
        now = datetime.datetime.now()
        LCD1602.write(0, 0, now.strftime('%Y/%m/%d %H:%M'))
        LCD1602.write(0, 1, 'Waiting motion...')
