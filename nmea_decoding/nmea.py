import serial
import pynmea2
import pynmea2.types.talker as tk


def track(lat, long):
    print(f'location: {lat}, {long}')


def datapr(msg):
    if isinstance(msg, tk.RMC):
        print('RMC:')
        print(f'\tLat / Long\t{msg.latitude} / {msg.longitude}')
        print(f'\tMode: {msg.mode}')
    elif isinstance(msg, tk.GSA):
        print('GSA:')
        print(f'\tPDOP: {msg.pdop}')
        print(f'\tHDOP: {msg.hdop}')
        print(f'\tVDOP: {msg.vdop}')
    elif isinstance(msg, tk.GGA):
        print('GGA:')
        print(f'\tHDOP: {msg.horizontal_dil}')
        print(f'\tFix: {msg.gps_qual}')
        print(f'\tSats: {msg.num_sats}')
        print(f'\tMode: {msg.mode}')
        print(f'\tMode Type: {msg.mode_fix_type}')
    elif isinstance(msg, tk.VTG):
        print('VTG:')
        print(f'\tHeading: {msg.true_track}{msg.true_track_sym}')
        print(f'\tSpeed: {msg.spd_over_grnd_kmph}{msg.spd_over_grnd_kmph_sym}')
        print(f'\tMode: {msg.faa_mode}')


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
    while True:
        try:
            msg = pynmea2.parse(ser.readline().decode("ascii"))
            datapr(msg)
        except serial.SerialException as e:
            print(f'Device error: {e}')
            break
        except pynmea2.ParseError as e:
            print(f'Parse error: {e}')



