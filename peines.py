
import xlrd
import matplotlib.pyplot as plt
import openpyxl

filePath = r'C:\Users\apb19\Documents\PAE Peines.xlsx'
# filePath = r'C:\\Users\\alexa\\OneDrive\\Escritorio\\TELECOS\\PAE\\PAE_peines.xlsx'
openFile = xlrd.open_workbook(filePath)
sheet = openFile.sheet_by_name("59")

# Esta función tiene por objetivo leer los parámetros del excel en función del click del usuario

# This function lets us know the impedance value


def getZ(samples, freq, dist):
    if samples == 0:  # Esto es para MM
        if dist == 0:  # Esto es para no distancia
            if freq == 0:  # Esto es para 10Hz
                Z = sheet.col_values(2, 415, 616)
            elif freq == 1:  # Esto es para 1 Hz
                Z = sheet.col_values(10, 415, 616)
            elif freq == 2:  # Esto es para 0.1Hz
                Z = sheet.col_values(18, 415, 616)
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 1:  # Para 1cm
            if freq == 0:  # Esto es para 10Hz
                Z = sheet.col_values(50, 415, 616)
            elif freq == 1:  # Esto es para 1 Hz
                Z = sheet.col_values(58, 415, 616)
            elif freq == 2:  # Esto es para 0.1Hz
                Z = 0  # NO VALUES
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 2:  # Para 5cm
            if freq == 0:  # Esto es para 10Hz
                Z = sheet.col_values(26, 415, 616)
            elif freq == 1:  # Esto es para 1 Hz
                Z = sheet.col_values(34, 415, 616)
            elif freq == 2:  # Esto es para 0.1Hz
                Z = 0  # NO VALUES
            else:
                print("El numero introducido es incorrecto!")
    elif samples == 1:  # Para M1
        if dist == 0:  # Esto es para no distancia
            if freq == 0:  # Esto es para 10Hz
                Z = sheet.col_values(2, 4, 204)
            elif freq == 1:  # Esto es para 1 Hz
                Z = sheet.col_values(10, 4, 204)
            elif freq == 2:  # Esto es para 0.1Hz
                Z = sheet.col_values(18, 4, 204)
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 1:  # Para 1cm
            if freq == 0:  # Esto es para 10Hz
                Z = sheet.col_values(50, 4, 204)
            elif freq == 1:  # Esto es para 1 Hz
                Z = sheet.col_values(58, 4, 204)
            elif freq == 2:  # Esto es para 0.1Hz
                Z = 0
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 2:  # Para 5cm
            if freq == 0:  # Esto es para 10Hz
                Z = sheet.col_values(26, 4, 204)
            elif freq == 1:  # Esto es para 1 Hz
                Z = sheet.col_values(34, 4, 204)
            elif freq == 2:  # Esto es para 0.1Hz
                Z = 0
            else:
                print("El numero introducido es incorrecto!")
    elif samples == 2:  # Para M2
        if dist == 0:  # Esto es para no distancia
            if freq == 0:  # Esto es para 10Hz
                Z = sheet.col_values(2, 209, 410)
            elif freq == 1:  # Esto es para 1 Hz
                Z = sheet.col_values(10, 209, 410)
            elif freq == 2:  # Esto es para 0.1Hz
                Z = sheet.col_values(18, 209, 410)
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 1:  # Para 1cm
            if freq == 0:  # Esto es para 10Hz
                Z = sheet.col_values(50, 209, 410)
            elif freq == 1:  # Esto es para 1 Hz
                Z = sheet.col_values(58, 209, 410)
            elif freq == 2:  # Esto es para 0.1Hz
                Z = 0
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 2:  # Para 5cm
            if freq == 0:  # Esto es para 10Hz
                Z = sheet.col_values(26, 209, 410)
            elif freq == 1:  # Esto es para 1 Hz
                Z = sheet.col_values(34, 209, 410)
            elif freq == 2:  # Esto es para 0.1Hz
                Z = 0
            else:
                print("El numero introducido es incorrecto!")

    return Z

# This function lets us know the phase value


def getPh(samples, freq, dist):
    if samples == 0:  # Esto es para MM
        if dist == 0:  # Esto es para no distancia
            if freq == 0:  # Esto es para 10Hz
                Ph = sheet.col_values(3, 415, 616)
            elif freq == 1:  # Esto es para 1 Hz
                Ph = sheet.col_values(11, 415, 616)
            elif freq == 2:  # Esto es para 0.1Hz
                Ph = sheet.col_values(19, 415, 616)
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 1:  # Para 1cm
            if freq == 0:  # Esto es para 10Hz
                Ph = sheet.col_values(51, 415, 616)
            elif freq == 1:  # Esto es para 1 Hz
                Ph = sheet.col_values(59, 415, 616)
            elif freq == 2:  # Esto es para 0.1Hz
                Ph = 0  # NO VALUES
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 2:  # Para 5cm
            if freq == 0:  # Esto es para 10Hz
                Ph = sheet.col_values(27, 415, 616)
            elif freq == 1:  # Esto es para 1 Hz
                Ph = sheet.col_values(35, 415, 616)
            elif freq == 2:  # Esto es para 0.1Hz
                Ph = 0  # NO VALUES
            else:
                print("El numero introducido es incorrecto!")
    elif samples == 1:  # Para M1
        if dist == 0:  # Esto es para no distancia
            if freq == 0:  # Esto es para 10Hz
                Ph = sheet.col_values(3, 4, 204)
            elif freq == 1:  # Esto es para 1 Hz
                Ph = sheet.col_values(11, 4, 204)
            elif freq == 2:  # Esto es para 0.1Hz
                Ph = sheet.col_values(19, 4, 204)
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 1:  # Para 1cm
            if freq == 0:  # Esto es para 10Hz
                Ph = sheet.col_values(51, 4, 204)
            elif freq == 1:  # Esto es para 1 Hz
                Ph = sheet.col_values(59, 4, 204)
            elif freq == 2:  # Esto es para 0.1Hz
                Ph = 0
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 2:  # Para 5cm
            if freq == 0:  # Esto es para 10Hz
                Ph = sheet.col_values(27, 4, 204)
            elif freq == 1:  # Esto es para 1 Hz
                Ph = sheet.col_values(35, 4, 204)
            elif freq == 2:  # Esto es para 0.1Hz
                Ph = 0
            else:
                print("El numero introducido es incorrecto!")
    elif samples == 2:  # Para M2
        if dist == 0:  # Esto es para no distancia
            if freq == 0:  # Esto es para 10Hz
                Ph = sheet.col_values(3, 209, 410)
            elif freq == 1:  # Esto es para 1 Hz
                Ph = sheet.col_values(11, 209, 410)
            elif freq == 2:  # Esto es para 0.1Hz
                Ph = sheet.col_values(19, 209, 410)
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 1:  # Para 1cm
            if freq == 0:  # Esto es para 10Hz
                Ph = sheet.col_values(51, 209, 410)
            elif freq == 1:  # Esto es para 1 Hz
                Ph = sheet.col_values(59, 209, 410)
            elif freq == 2:  # Esto es para 0.1Hz
                Ph = 0
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 2:  # Para 5cm
            if freq == 0:  # Esto es para 10Hz
                Ph = sheet.col_values(27, 209, 410)
            elif freq == 1:  # Esto es para 1 Hz
                Ph = sheet.col_values(35, 209, 410)
            elif freq == 2:  # Esto es para 0.1Hz
                Ph = 0
            else:
                print("El numero introducido es incorrecto!")

    return Ph

# This function lets us know the real impedance value


def getZ1(samples, freq, dist):
    if samples == 0:  # Esto es para MM
        if dist == 0:  # Esto es para no distancia
            if freq == 0:  # Esto es para 10Hz
                Z1 = sheet.col_values(4, 415, 616)
            elif freq == 1:  # Esto es para 1 Hz
                Z1 = sheet.col_values(12, 415, 616)
            elif freq == 2:  # Esto es para 0.1Hz
                Z1 = sheet.col_values(20, 415, 616)
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 1:  # Para 1cm
            if freq == 0:  # Esto es para 10Hz
                Z1 = sheet.col_values(52, 415, 616)
            elif freq == 1:  # Esto es para 1 Hz
                Z1 = sheet.col_values(60, 415, 616)
            elif freq == 2:  # Esto es para 0.1Hz
                Z1 = 0  # NO VALUES
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 2:  # Para 5cm
            if freq == 0:  # Esto es para 10Hz
                Z1 = sheet.col_values(28, 415, 616)
            elif freq == 1:  # Esto es para 1 Hz
                Z1 = sheet.col_values(36, 415, 616)
            elif freq == 2:  # Esto es para 0.1Hz
                Z1 = 0  # NO VALUES
            else:
                print("El numero introducido es incorrecto!")
    elif samples == 1:  # Para M1
        if dist == 0:  # Esto es para no distancia
            if freq == 0:  # Esto es para 10Hz
                Z1 = sheet.col_values(4, 4, 204)
            elif freq == 1:  # Esto es para 1 Hz
                Z1 = sheet.col_values(12, 4, 204)
            elif freq == 2:  # Esto es para 0.1Hz
                Z1 = sheet.col_values(20, 4, 204)
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 1:  # Para 1cm
            if freq == 0:  # Esto es para 10Hz
                Z1 = sheet.col_values(52, 4, 204)
            elif freq == 1:  # Esto es para 1 Hz
                Z1 = sheet.col_values(60, 4, 204)
            elif freq == 2:  # Esto es para 0.1Hz
                Z1 = 0
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 2:  # Para 5cm
            if freq == 0:  # Esto es para 10Hz
                Z1 = sheet.col_values(28, 4, 204)
            elif freq == 1:  # Esto es para 1 Hz
                Z1 = sheet.col_values(36, 4, 204)
            elif freq == 2:  # Esto es para 0.1Hz
                Z1 = 0
            else:
                print("El numero introducido es incorrecto!")
    elif samples == 2:  # Para M2
        if dist == 0:  # Esto es para no distancia
            if freq == 0:  # Esto es para 10Hz
                Z1 = sheet.col_values(4, 209, 410)
            elif freq == 1:  # Esto es para 1 Hz
                Z1 = sheet.col_values(12, 209, 410)
            elif freq == 2:  # Esto es para 0.1Hz
                Z1 = sheet.col_values(20, 209, 410)
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 1:  # Para 1cm
            if freq == 0:  # Esto es para 10Hz
                Z1 = sheet.col_values(52, 209, 410)
            elif freq == 1:  # Esto es para 1 Hz
                Z1 = sheet.col_values(60, 209, 410)
            elif freq == 2:  # Esto es para 0.1Hz
                Z1 = 0
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 2:  # Para 5cm
            if freq == 0:  # Esto es para 10Hz
                Z1 = sheet.col_values(28, 209, 410)
            elif freq == 1:  # Esto es para 1 Hz
                Z1 = sheet.col_values(36, 209, 410)
            elif freq == 2:  # Esto es para 0.1Hz
                Z1 = 0
            else:
                print("El numero introducido es incorrecto!")
    return Z1

# This function lets us know the imaginary impedance value


def getZ2(samples, freq, dist):

        if samples == 0:  # Esto es para MM
            if dist == 0:  # Esto es para no distancia
                if freq == 0:  # Esto es para 10Hz
                    Z2 = sheet.col_values(5, 415, 616)
                elif freq == 1:  # Esto es para 1 Hz
                    Z2 = sheet.col_values(13, 415, 616)
                elif freq == 2:  # Esto es para 0.1Hz
                    Z2 = sheet.col_values(21, 415, 616)
                else:
                    print("El numero introducido es incorrecto!")
            elif dist == 1:  # Para 1cm
                if freq == 0:  # Esto es para 10Hz
                    Z2 = sheet.col_values(53, 415, 616)
                elif freq == 1:  # Esto es para 1 Hz
                    Z2 = sheet.col_values(61, 415, 616)
                elif freq == 2:  # Esto es para 0.1Hz
                    Z2 = 0  # NO VALUES
                else:
                    print("El numero introducido es incorrecto!")
            elif dist == 2:  # Para 5cm
                if freq == 0:  # Esto es para 10Hz
                    Z2 = sheet.col_values(29, 415, 616)
                elif freq == 1:  # Esto es para 1 Hz
                    Z2 = sheet.col_values(37, 415, 616)
                elif freq == 2:  # Esto es para 0.1Hz
                    Z2 = 0  # NO VALUES
                else:
                    print("El numero introducido es incorrecto!")
        elif samples == 1:  # Para M1
            if dist == 0:  # Esto es para no distancia
                if freq == 0:  # Esto es para 10Hz
                    Z2 = sheet.col_values(5, 4, 204)
                elif freq == 1:  # Esto es para 1 Hz
                    Z2 = sheet.col_values(13, 4, 204)
                elif freq == 2:  # Esto es para 0.1Hz
                    Z2 = sheet.col_values(21, 4, 204)
                else:
                    print("El numero introducido es incorrecto!")
            elif dist == 1:  # Para 1cm
                if freq == 0:  # Esto es para 10Hz
                    Z2 = sheet.col_values(53, 4, 204)
                elif freq == 1:  # Esto es para 1 Hz
                    Z2 = sheet.col_values(61, 4, 204)
                elif freq == 2:  # Esto es para 0.1Hz
                    Z2 = 0
                else:
                    print("El numero introducido es incorrecto!")
            elif dist == 2:  # Para 5cm
                if freq == 0:  # Esto es para 10Hz
                    Z2 = sheet.col_values(29, 4, 204)
                elif freq == 1:  # Esto es para 1 Hz
                    Z2 = sheet.col_values(37, 4, 204)
                elif freq == 2:  # Esto es para 0.1Hz
                    Z2 = 0
                else:
                    print("El numero introducido es incorrecto!")
        elif samples == 2:  # Para M2
            if dist == 0:  # Esto es para no distancia
                if freq == 0:  # Esto es para 10Hz
                    Z2 = sheet.col_values(5, 209, 410)
                elif freq == 1:  # Esto es para 1 Hz
                    Z2 = sheet.col_values(13, 209, 410)
                elif freq == 2:  # Esto es para 0.1Hz
                    Z2 = sheet.col_values(21, 209, 410)
                else:
                    print("El numero introducido es incorrecto!")
            elif dist == 1:  # Para 1cm
                if freq == 0:  # Esto es para 10Hz
                    Z2 = sheet.col_values(53, 209, 410)
                elif freq == 1:  # Esto es para 1 Hz
                    Z2 = sheet.col_values(61, 209, 410)
                elif freq == 2:  # Esto es para 0.1Hz
                    Z2 = 0
                else:
                    print("El numero introducido es incorrecto!")
            elif dist == 2:  # Para 5cm
                if freq == 0:  # Esto es para 10Hz
                    Z2 = sheet.col_values(29, 209, 410)
                elif freq == 1:  # Esto es para 1 Hz
                    Z2 = sheet.col_values(37, 209, 410)
                elif freq == 2:  # Esto es para 0.1Hz
                    Z2 = 0
                else:
                    print("El numero introducido es incorrecto!")

        return Z2

    # This function lets us know the frecuency value


def getF(samples, freq, dist):

        if samples == 0:  # Esto es para MM
            if dist == 0:  # Esto es para no distancia
                if freq == 0:  # Esto es para 10Hz
                    f = sheet.col_values(1, 415, 616)
                elif freq == 1:  # Esto es para 1 Hz
                    f = sheet.col_values(9, 415, 616)
                elif freq == 2:  # Esto es para 0.1Hz
                    f = sheet.col_values(17, 415, 616)
                else:
                    print("El numero introducido es incorrecto!")
            elif dist == 1:  # Para 1cm
                if freq == 0:  # Esto es para 10Hz
                    f = sheet.col_values(49, 415, 616)
                elif freq == 1:  # Esto es para 1 Hz
                    f = sheet.col_values(57, 415, 616)
                elif freq == 2:  # Esto es para 0.1Hz
                    f = 0  # NO VALUES
                else:
                    print("El numero introducido es incorrecto!")
            elif dist == 2:  # Para 5cm
                if freq == 0:  # Esto es para 10Hz
                    f = sheet.col_values(25, 415, 616)
                elif freq == 1:  # Esto es para 1 Hz
                    f = sheet.col_values(33, 415, 616)
                elif freq == 2:  # Esto es para 0.1Hz
                    f = 0  # NO VALUES
                else:
                    print("El numero introducido es incorrecto!")
        elif samples == 1:  # Para M1
            if dist == 0:  # Esto es para no distancia
                if freq == 0:  # Esto es para 10Hz
                    f = sheet.col_values(1, 4, 204)
                elif freq == 1:  # Esto es para 1 Hz
                    f = sheet.col_values(9, 4, 204)
                elif freq == 2:  # Esto es para 0.1Hz
                    f = sheet.col_values(17, 4, 204)
                else:
                    print("El numero introducido es incorrecto!")
            elif dist == 1:  # Para 1cm
                if freq == 0:  # Esto es para 10Hz
                    f = sheet.col_values(49, 4, 204)
                elif freq == 1:  # Esto es para 1 Hz
                    f = sheet.col_values(57, 4, 204)
                elif freq == 2:  # Esto es para 0.1Hz
                    f = 0
                else:
                    print("El numero introducido es incorrecto!")
            elif dist == 2:  # Para 5cm
                if freq == 0:  # Esto es para 10Hz
                    f = sheet.col_values(25, 4, 204)
                elif freq == 1:  # Esto es para 1 Hz
                    f = sheet.col_values(33, 4, 204)
                elif freq == 2:  # Esto es para 0.1Hz
                    f = 0
                else:
                    print("El numero introducido es incorrecto!")
        elif samples == 2:  # Para M2
            if dist == 0:  # Esto es para no distancia
                if freq == 0:  # Esto es para 10Hz
                    f = sheet.col_values(1, 209, 410)
                elif freq == 1:  # Esto es para 1 Hz
                    f = sheet.col_values(9, 209, 410)
                elif freq == 2:  # Esto es para 0.1Hz
                    f = sheet.col_values(17, 209, 410)
                else:
                    print("El numero introducido es incorrecto!")
            elif dist == 1:  # Para 1cm
                if freq == 0:  # Esto es para 10Hz
                    f = sheet.col_values(49, 209, 410)
                elif freq == 1:  # Esto es para 1 Hz
                    f = sheet.col_values(57, 209, 410)
                elif freq == 2:  # Esto es para 0.1Hz
                    f = 0
                else:
                    print("El numero introducido es incorrecto!")
            elif dist == 2:  # Para 5cm
                if freq == 0:  # Esto es para 10Hz
                    f = sheet.col_values(25, 209, 410)
                elif freq == 1:  # Esto es para 1 Hz
                    f = sheet.col_values(33, 209, 410)
                elif freq == 2:  # Esto es para 0.1Hz
                    f = 0
                else:
                    print("El numero introducido es incorrecto!")
        return f


# This function lets us know the capacity value

def getC(samples, freq, dist):
    if samples == 0:  # Esto es para MM
        if dist == 0:  # Esto es para no distancia
            if freq == 0:  # Esto es para 10Hz
                C = sheet.col_values(6, 415, 616)
            elif freq == 1:  # Esto es para 1 Hz
                C = sheet.col_values(14, 415, 616)
            elif freq == 2:  # Esto es para 0.1Hz
                C = sheet.col_values(22, 415, 616)
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 1:  # Para 1cm
            if freq == 0:  # Esto es para 10Hz
                C = sheet.col_values(54, 415, 616)
            elif freq == 1:  # Esto es para 1 Hz
                C = sheet.col_values(62, 415, 616)
            elif freq == 2:  # Esto es para 0.1Hz
                C = 0  # NO VALUES
            else:
                print("El numero introducido es incorrecto!")
        elif dist == 2:  # Para 5cm
            if freq == 0:  # Esto es para 10Hz
                C = sheet.col_values(30, 415, 616)
            elif freq == 1:  # Esto es para 1 Hz
                C = sheet.col_values(38, 415, 616)
            elif freq == 2:  # Esto es para 0.1Hz
                C = 0  # NO VALUES
            else:
                print("El numero introducido es incorrecto!")
    elif samples == 1: # Para M1
        if dist == 0: #Esto es para no distancia
            if freq == 0: # Esto es para 10Hz
                C = sheet.col_values(6,4,204)
            elif freq == 1: #Esto es para 1 Hz
                C = sheet.col_values(14,4,204) 
            elif freq == 2: # Esto es para 0.1Hz
                C = sheet.col_values(22,4,204)
            else:
                print ("El numero introducido es incorrecto!")
        elif dist == 1: #Para 1cm
            if freq == 0: # Esto es para 10Hz
                C = sheet.col_values(54,4,204)
            elif freq == 1: #Esto es para 1 Hz
                C = sheet.col_values(62,4,204) 
            elif freq == 2: # Esto es para 0.1Hz
                C = 0
            else:
                print ("El numero introducido es incorrecto!")
        elif dist == 2: #Para 5cm
            if freq == 0: # Esto es para 10Hz
                C = sheet.col_values(30,4,204)
            elif freq == 1: #Esto es para 1 Hz
                C = sheet.col_values(38,4,204) 
            elif freq == 2: # Esto es para 0.1Hz
                C = 0
            else:
                print ("El numero introducido es incorrecto!")
    elif samples == 2: # Para M2
        if dist == 0: #Esto es para no distancia
            if freq == 0: # Esto es para 10Hz
                C = sheet.col_values(6,209,410)
            elif freq == 1: #Esto es para 1 Hz
                C = sheet.col_values(14,209,410)  
            elif freq == 2: # Esto es para 0.1Hz
                C = sheet.col_values(22,209,410)
            else:
                print ("El numero introducido es incorrecto!")
        elif dist == 1: #Para 1cm
            if freq == 0: # Esto es para 10Hz
                C = sheet.col_values(54,209,410)
            elif freq == 1: #Esto es para 1 Hz
                C = sheet.col_values(62,209,410) 
            elif freq == 2: # Esto es para 0.1Hz
                C = 0
            else:
                print ("El numero introducido es incorrecto!")
        elif dist == 2: #Para 5cm
            if freq == 0: # Esto es para 10Hz
                C = sheet.col_values(30,209,410)
            elif freq == 1: #Esto es para 1 Hz
                C = sheet.col_values(38,209,410) 
            elif freq == 2: # Esto es para 0.1Hz
                C = 0
            else:
                print ("El numero introducido es incorrecto!")
    return C 
