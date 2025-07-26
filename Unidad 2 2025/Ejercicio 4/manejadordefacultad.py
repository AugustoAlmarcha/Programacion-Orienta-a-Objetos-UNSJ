from clasefacultad import *
import numpy as np
import csv

class Manejadorfacultad:
    __arreglofacultad:np.ndarray
    
    def __init__(self):
        self.__dimension=10
        self.__incremento=5
        self.__cantidad=0
        self.__arreglofacultad=np.zeros(self.__dimension,dtype=Facultad)
        
    def agregarfacultad(self,facultad):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglofacultad.resize(self.__dimension)
        self.__arreglofacultad[self.__cantidad]=facultad
        self.__cantidad+=1
    
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\2025\Ejercicio 4\Facultades.csv")
            reader=csv.reader(archivo,delimiter=";")
            next(reader)
            for fila in reader:
                self.agregarfacultad(Facultad(int(fila[0]),fila[1],fila[2],fila[3],fila[4]))
            archivo.close()
        except FileNotFoundError:
            print("El archivo CSV no se encontró.")
        except Exception as e:
            print("Error al leer el archivo CSV:", e)
    
    def mostrar(self):
        for item in range(self.__cantidad):
            print(self.__arreglofacultad[item])
    
    def buscarfacultad(self,codigo):
        band=False
        i=0
        while band is False and i<self.__cantidad:
            if codigo == self.__arreglofacultad[i].getcodigofacultad():
                band=True
                nombre=self.__arreglofacultad[i].getnombre()
                return nombre
            i+=1
        if band is False:
            return None
    
    def contarfacultad(self,codigo):
        band=False
        i=0
        while band is False and i<self.__cantidad:
            if codigo == self.__arreglofacultad[i].getcodigofacultad():
                band=True
                return self.__arreglofacultad[i]
            i+=1
        if band is False:
            return None
        
    def buscarfacultadxnombre(self,carrera):
        i=0
        band=False
        nombre=input("Ingrese el nombre de la facultad que quiere saber las carreras")
        while i<self.__cantidad and band is False:
            if nombre == self.__arreglofacultad[i].getnombre():
                band=True
            else:
                i+=1
        if band is False:
            print("No se encontro la facultad que busca")
        else:
            carrera.mostrarcarrerasespecifico(self.__arreglofacultad[i])
        
            
    
    
            
            
# if __name__=="__main__":
#     facultadx=Manejadorfacultad()
#     facultadx.cargarcsv()
#     facultadx.mostrar()
            
            