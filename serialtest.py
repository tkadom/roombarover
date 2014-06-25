import serial
from time import sleep

port = '/dev/ttyO4'
ser = serial.Serial(port, 115200, timeout=0)

while True:
    ser.write("hello world")
    print ser.readline()

ser.close()
