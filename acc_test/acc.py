import serial
import pynmea2
import pynmea2.types.talker as tk
import matplotlib.pyplot as plt


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
    fix = False
    pos_data = ([], [])
    dops = ([], [], [])

    print('waiting for fix...')
    while True:
        try:
            msg = pynmea2.parse(ser.readline().decode("ascii"))
            if fix:
                if isinstance(msg, tk.RMC):
                    pos_data[0].append(float(msg.longitude))
                    pos_data[1].append(float(msg.latitude))
                elif isinstance(msg, tk.GSA):
                    dops[0].append(float(msg.pdop))
                    dops[1].append(float(msg.hdop))
                    dops[2].append(float(msg.vdop))
            else:
                if isinstance(msg, tk.RMC):
                    if msg.status != 'V':
                        fix = True
                        print("got a fix")
        except serial.SerialException as e:
            print(f'Device error: {e}')
            break
        except pynmea2.ParseError as e:
            print(f'Parse error: {e}')
        except KeyboardInterrupt as e:
            break
    plt.scatter(pos_data[0], pos_data[1])
    plt.title('positional data')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()

    n, b, p = plt.hist(dops, 40, density=True, alpha=0.8)
    plt.title(f'Distribution of DOPs')
    plt.legend(['PDOP', 'HDOP', 'VDOP'])
    plt.show()

    t = range(0,len(dops[0]))
    plt.plot(t, dops[0],'r', t, dops[1], 'b', t, dops[2], 'g')
    plt.legend(['PDOP', 'HDOP', 'VDOP'])
    plt.xlabel('Time')
    plt.ylabel('DOPs')
    plt.show()



