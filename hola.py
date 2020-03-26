
import numpy as np
import matplotlib.pyplot as plt
from peines import getF, getC, getPh, getZ, getZ1, getZ2



def ploteo(number):
    f = getF(number) 
    Z = getZ(number) 
    Ph = getPh(number)
    Z1 = getZ1(number)
    Z2 = getZ2(number)
    C = getC(number)

    plt.title('Z(f)')
    plt.xlabel('Frecuency (Hz)')
    plt.ylabel('Impedance (Ohms)')
    plt.loglog(f,Z, 'r.')
    plt.figure()

    plt.title('Ph(f)')
    plt.xlabel('Frequency(Hz)')
    plt.ylabel('Phase (º)')
    plt.plot(f,Ph,'r.')
    plt.figure()
    
    plt.title('Z2(Z1)')
    plt.xlabel('Module (Ohms)')
    plt.ylabel('Fase (º)')
    plt.loglog(Z2,Z1, 'r.')
    plt.figure()
    
    plt.title('C(f)')
    plt.xlabel('Frecuency (Hz)')
    plt.ylabel('Capacity (F)')
    plt.plot(f,C, 'r.')
    plt.show()


    

