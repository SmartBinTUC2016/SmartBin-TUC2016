import serial
import time

class ArduinoSerial():
    def __init__(self):
        self.ser = serial.Serial()

    '''
    Handles the connection to serial port
    '''
    def connect(self,baudrate, port, timeout = None):
        self.ser.baudrate = baudrate
        self.ser.port = port
        self.ser.timeout = timeout
        try:
            print('Attempting to connect to: {0}').format(self.ser.name)
            self.ser.open()
        except:
            print('Connection unsuccessful')
        if self.ser.is_open:
            print('Connection successful')
        else:
            print('Connection unsuccessful')
        return

    '''
    Closes serial port
    '''
    def close(self):
        self.ser.close
        if self.ser.is_open:
            print('Could not close connection')
        else:
            print('Connection closed successfully')
        return

    '''
    Writes to serial port
    '''
    def write(self, message):
        try:
            self.ser.write(message)
        except:
            print('Error writing to serial')
        return

    '''
    Reads from serial port
    '''
    def read(self):
        message = None
        try:
            message = str(self.ser.readline()).strip('\n')
        except:
            print('Error reading line from serial')
        return message
