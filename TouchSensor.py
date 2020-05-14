import sys
import time
import serial
import serial.tools.list_ports

def ComportAvailable():
    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)
    #print("Connected COM ports: " + str(connected)) only for test purpose
    return connected

def ESP32Connect(port, baud):
    arduino = serial.Serial(port, baudrate=baud, timeout=1.0)
    return arduino

def ESP32Read(arduino):
    #data = []                     # empty list to store the data
    #for i in range(5):
    b = arduino.readline()
    string_n = b.decode()
    string = string_n.rstrip()
        #flt = float(string)        
        #print(flt)
        #data.append(string)
    time.sleep(0.1) 
    return string   