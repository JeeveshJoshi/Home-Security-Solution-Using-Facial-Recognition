import serial
import time
usbport = 'COM8'

ser = serial.Serial()
ser.port='COM8'
ser.baudrate=9600
ser.timeout=1
if ser.isOpen()==False:
    print("Serial was closed")
    ser.open()
    print("Serial now open")
    time.sleep(2)
    ser.write(70)
    time.sleep(2)
    #ser.write(120)
else:
    print("Serial port already open")
