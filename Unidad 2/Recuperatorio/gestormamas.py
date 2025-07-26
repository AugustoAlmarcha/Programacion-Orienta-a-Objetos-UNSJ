import csv 
import numpy as np
from clasemama import *

class GestorMamas:
    __arreglomamas:np.ndarray
    __cantidad:int
    __dimension:int
    __incremento:int
    
    def __init__(self):
        self.__cantidad=0
        self.__dimension=10
        self.__incremento=5
        self.__arreglomamas=np.empty(self.__dimension,dtype=Mama)
        
    def agregarMama(self,mama):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglomamas.resize(self.__dimension)
        self.__arreglomamas[self.__cantidad]=mama
        self.__cantidad+=1
    
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\Recuperatorio\Mamas.csv")
            reader=csv.reader(archivo,delimiter=';')
            for fila in reader:
                self.agregarMama(Mama(fila[0],int(fila[1]),fila[2]))
            archivo.close()
        except FileNotFoundError:
            print("El archivo no se encontro")
        except Exception as error:
            print(f"Error en la carga de datos {error}")
    
    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__arreglomamas[i])
            
    def mostrardatosmamas(self,dni,nacimientos):
        band=False
        i=0
        while band is False and i<self.__cantidad:
            if self.__arreglomamas[i].getDni()==dni:
                print(self.__arreglomamas[i].getNya())
                print(self.__arreglomamas[i].getEdad())
                nacimientos.mostrarnacimientos(dni)
                band=True
            i+=1
        if band==False:
            print("No se encontro el dni")
            
    def mostrartodomamas(self,dni):
        band=False
        i=0
        while band is False and i<self.__cantidad:
            if self.__arreglomamas[i].getDni()==dni:
                print(f"{self.__arreglomamas[i]}, tuvo parto multiple")
                band=True
            i+=1
        if band==False:
            print("No se encontro el dni")
    
    
        
    
# if __name__=="__main__":
#     gestor=GestorMamas()
#     gestor.cargarcsv()
#     gestor.mostrar()
        