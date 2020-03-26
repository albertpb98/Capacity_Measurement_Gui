
import xlrd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl

filePath = r'C:\Users\apb19\Documents\PAE Peines.xlsx'
openFile = xlrd.open_workbook(filePath)
sheet = openFile.sheet_by_name("59")

#print("Num de filas", sheet.nrows)
#print("Num de columnas",sheet.ncols)
#Cuidado con los cambios

def getZ(number):
    if number == 1: # Esto es para 10Hz
     Z = sheet.col_values(2,415,616)
     print(Z)
    elif number == 2: #Esto es para 1 Hz
     Z = sheet.col_values(9,415,616) 
    
    elif number == 3: # Esto es para 0.1Hz
     Z = sheet.col_values(15,415,616)
    else:
     print ("El numero introducido es incorrecto!")

    return Z
         

def getPh(number):
    if number == 1: # Esto es para 10Hz
     Ph = sheet.col_values(3,415,616)
     
    elif number == 2: # Esto es para 1 Hz
     Ph = sheet.col_values(10,415,616) 
    
    elif number == 3: # Esto es para 0.1Hz
     Ph = sheet.col_values(16,415,616)
    else:
     print ("El numero introducido es incorrecto!")
        
    return Ph 

def getZ1(number):
    if number == 1: # Esto es para 10Hz
     Z1 = sheet.col_values(4,415,616)
    elif number == 2: #Esto es para 1 Hz
     Z1 = sheet.col_values(11,415,616) 
    
    elif number == 3: # Esto es para 0.1Hz
     Z1 = sheet.col_values(17,415,616)
    else:
        print ("El numero introducido es incorrecto!")
        
    return Z1

def getZ2(number):
    if number == 1: # Esto es para 10Hz
     Z2 = sheet.col_values(5,415,616)
    elif number == 2: #Esto es para 1 Hz
     Z2 = sheet.col_values(12,415,616) 
    
    elif number == 3: # Esto es para 0.1Hz
     Z2 = sheet.col_values(18,415,616)
    else:
        print ("El numero introducido es incorrecto!")
        
    return Z2 

def getF(number):
    if number == 1: # Esto es para 10Hz
     f = sheet.col_values(1,415,616)
     
    elif number == 2: #Esto es para 1 Hz
     f = sheet.col_values(8,415,616) 
    
    elif number == 3: # Esto es para 0.1Hz
     f = sheet.col_values(14,415,616)
    else:
        print ("El numero introducido es incorrecto!")
        
    return f 

def getC(number):
    if number == 1: # Esto es para 10Hz
     C = sheet.col_values(6,415,616)
     
    elif number == 2: # Esto es para 1 Hz
     C = sheet.col_values(13,415,616) 
    
    elif number == 3: # Esto es para 0.1Hz
     C = sheet.col_values(19,415,616)
    else:
        print ("El numero introducido es incorrecto!")
        
    return C 
   
#fa = sheet.col_values(8,415,616)
#Za = sheet.col_values(9,415,616)
#Pha = sheet.col_values(10,415,616)
#Z1a = sheet.col_values(11,415,616)
#Z2a = sheet.col_values(12,415,616)
#Ca = sheet.col_values(13,415,616)

#faa = sheet.col_values(14,415,616)
#Zaa = sheet.col_values(15,415,616)
#Phaa = sheet.col_values(16,415,616)
#Z1aa = sheet.col_values(17,415,616)
#Z2aa = sheet.col_values(18,415,616)
#Caa = sheet.col_values(19,415,616)


#print(f)
#for i in range(sheet.nrows):
 #               print(sheet.cell_value(i,1),"    ",sheet.cell_value(i,2))