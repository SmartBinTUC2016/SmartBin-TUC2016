from serialcom import *
ser  = ArduinoSerial()

def startSer():
    global ser
    ser.connect(port='/dev/cu.usbmodem1411', baudrate=115200)

def closeSer():
    global ser
    ser.close()
