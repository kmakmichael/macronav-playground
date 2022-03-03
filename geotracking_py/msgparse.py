import serial
import pynmea2


def get_coords():
    ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
    for i in range(0, 20):
        try:
            msg = pynmea2.parse(ser.readline().decode("ascii"))
            if isinstance(msg, pynmea2.types.talker.RMC):
                if msg.status == 'V':
                    continue
                else:
                    coords = (msg.longitude, msg.latitude)
                    return coords
        except serial.SerialException as e:
            print(f'Device error: {e}')
            break
        except pynmea2.ParseError as e:
            print(f'Parse error: {e}')
    return () # (181, 91)


def get_route(): 
    coords = ([], [])
    ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
    while True:
        try:
            msg = pynmea2.parse(ser.readline().decode("ascii"))
            if isinstance(msg, pynmea2.types.talker.RMC):
                if msg.status != 'V':
                    # print(f'recording ({msg.longitude}, {msg.latitude})')
                    coords[0].append(msg.longitude)
                    coords[1].append(msg.latitude)
        except serial.SerialException as e:
            print(f'Device error: {e}')
            break
        except pynmea2.ParseError as e:
            print(f'Parse error: {e}')
        except KeyboardInterrupt as e:
            print(f'interrupting after {len(coords)} points')
            return coords
        except UnicodeDecodeError as e:
            print(f'Decode error: {e}')
    return coords
