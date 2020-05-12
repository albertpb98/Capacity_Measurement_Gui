import sys
import serial
import serial.tools.list_ports

def ComportAvailable():
    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)
    #print("Connected COM ports: " + str(connected)) only for test purpose
    return connected

