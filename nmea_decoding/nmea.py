import serial
import pynmea2
import pynmea2.types.talker as tk


def track(lat, long):
    print(f'location: {lat}, {long}')


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
    while True:
        try:
            msg = pynmea2.parse(ser.readline().decode("ascii"))
            print(msg)
            if isinstance(msg, pynmea2.types.talker.RMC):
                if msg.status == 'V':
                    print('No fix, discarding message')
                else:
                    track(msg.latitude, msg.longitude)
        except serial.SerialException as e:
            print(f'Device error: {e}')
            break
        except pynmea2.ParseError as e:
            print(f'Parse error: {e}')



