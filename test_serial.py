import serial
import time

port = serial.Serial("/dev/serial0", baudrate=9600, timeout=20000, bytesize=serial.EIGHTBITS, parity=serial.PARITY_EVEN, stopbits = serial.STOPBITS_TWO)


port.write('760300')
