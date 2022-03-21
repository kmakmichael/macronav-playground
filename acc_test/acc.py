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
        print(f'\tMode: {msg.mode}')
        print(f'\tMode Type: {msg.mode_fix_type}')
        print(f'\tPDOP: {msg.pdop}')
        print(f'\tHDOP: {msg.hdop}')
        print(f'\tVDOP: {msg.vdop}')
    elif isinstance(msg, tk.GGA):
        print('GGA:')
        print(f'\tHDOP: {msg.horizontal_dil}')
        print(f'\tFix: {msg.gps_qual}')
        print(f'\tSats: {msg.num_sats}')
    elif isinstance(msg, tk.VTG):
        print('VTG:')
        print(f'\tHeading: {msg.true_track}{msg.true_track_sym}')
        print(f'\tSpeed: {msg.spd_over_grnd_kmph}{msg.spd_over_grnd_kmph_sym}')
        print(f'\tMode: {msg.faa_mode}')


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
    fix = False
    pos_data = ([], [])
    dops = {
        "pdop": [],
        "hdop": [],
        "vdop": []
    }

    while True:
        try:
            msg = pynmea2.parse(ser.readline().decode("ascii"))
            if fix:
                if isinstance(msg, tk.RMC):
                    pos_data[0].append(msg.longitude)
                    pos_data[1].append(msg.latitude)
                elif isinstance(msg, tk.GSA):
                    dops["pdop"].append(msg.pdop)
                    dops["hdop"].append(msg.hdop)
                    dops["vdop"].append(msg.vdop)
            else:
                if isinstance(msg, tk.RMC):
                    fix = (msg.status != 'V')
        except serial.SerialException as e:
            print(f'Device error: {e}')
            break
        except pynmea2.ParseError as e:
            print(f'Parse error: {e}')



