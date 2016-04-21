import serial
import sys
ser = serial.Serial('/dev/cu.usbmodem1411',9600)

while 1:
	print(ser.readline())
	ser.write('0')