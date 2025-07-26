import numpy as np
import csv
from clasefecha import *

class Gestorfechas:
    __arreglofechas=np.ndarray
    __cantidad:int
    __dimension:int
    __incremento:int
    
    def __init__(self):
        self.__cantidad=0
        self.__dimension=10
        self.__incremento=5
        self.__arreglofechas=np.zeros(self.__dimension,dtype=Fechadefutbol)
        
    def agregarfecha(self,fecha):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglofechas.resize(self.__dimension)
        self.__arreglofechas[self.__cantidad]=fecha
        self.__cantidad+=1
    
    def cargarcsv(self):
        try:
            archivo = open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\Ejercicio 5\fechasFutbol.csv")
            reader= csv.reader(archivo,delimiter=";")
            next(reader)
            for fila in reader:
                self.agregarfecha(Fechadefutbol(int(fila[0]),int(fila[1]),int(fila[2]),int(fila[3]),int(fila[4])))
            archivo.close()
        except Exception as e:
            print(e)
        except FileNotFoundError:
            print("El archivo no existe")
        
    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__arreglofechas[i])
            
    def buscarid(self,id):

            
            

# if __name__ == "__main__":       
#     fecha=Gestorfechas()
#     fecha.cargarcsv()
#     fecha.mostrar()

            