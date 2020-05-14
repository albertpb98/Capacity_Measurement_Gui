import sys
import time
import serial
import serial.tools.list_ports
from TouchSensor import ESP32Connect
import matplotlib.pyplot as plt

arduino = ESP32Connect('COM7', 115200)
time.sleep(2)
data = []
for i in range(50):
        b = arduino.readline()
        string_n = b.decode()
        string = string_n.rstrip()
        flt = float(string)        
        print(flt)
        data.append(flt)
        time.sleep(1) 


# if using a Jupyter notebook include

plt.plot(data)
plt.xlabel('Time (seconds)')
plt.ylabel('Potentiometer Reading')
plt.title('Potentiometer Reading vs. Time')
plt.show()