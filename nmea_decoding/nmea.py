import serial


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
    print(ser.readline())
