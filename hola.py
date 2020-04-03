
import numpy as np
import matplotlib.pyplot as plt
from peines import getF, getC, getPh, getZ, getZ1, getZ2
#More imports may be added

def ploteoZF(samples, freq, dist):
    plt.clf()
    f = getF(samples, freq, dist) 
    Z = getZ(samples, freq, dist)
    plt.title('Impedance - Frequency')
    plt.xlabel('Frecuency (Hz)')
    plt.ylabel('Impedance (Ohms)')
    plt.loglog(f,Z, 'r.')
    plt.show() #plt.show() es bloqueante. Hasta que no cierre una no se mostrará la otra gráfica.

def ploteoPhF(samples, freq, dist):
    plt.clf()
    Ph = getPh(samples, freq, dist)
    f = getF(samples, freq, dist)
    plt.title('Phase - Frequency')
    plt.xlabel('Frequency(Hz)')
    plt.ylabel('Phase (º)')
    plt.plot(f,Ph,'r.')
    plt.show() #plt.show() es bloqueante. Hasta que no cierre una no se mostrará la otra gráfica.

def ploteoZ1Z2(samples, freq, dist):
    plt.clf()
    Z1 = getZ1(samples, freq, dist)
    Z2 = getZ2(samples, freq, dist)
    plt.title('Module - Phase')
    plt.xlabel('Module (Ohms)')
    plt.ylabel('Fase (º)')
    plt.loglog(Z2,Z1, 'r.')
    plt.show() #plt.show() es bloqueante. Hasta que no cierre una no se mostrará la otra gráfica.

def ploteoCF(samples, freq, dist):
    plt.clf()
    C = getC(samples, freq, dist)
    f = getF(samples, freq, dist)
    plt.title('Capacity - Frequency')
    plt.xlabel('Frecuency (Hz)')
    plt.ylabel('Capacity (F)')
    plt.plot(f,C, 'r.')
    plt.show() #plt.show() es bloqueante. Hasta que no cierre una no se mostrará la otra gráfica.

