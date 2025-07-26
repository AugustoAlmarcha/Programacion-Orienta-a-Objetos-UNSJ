import csv
import numpy as np
from clasecancha import *

class Gestorcanchas:
    __arreglocanchas:np.ndarray
    __dimension:int
    __cantidad:int
    __incremento:int
    
    def __init__(self):
        self.__dimension=6
        self.__arreglocanchas=np.empty(self.__dimension,dtype=Cancha)
        self.__cantidad=0
        self.__incremento=5
        
    def agregarCancha(self,cancha:Cancha):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglocanchas.resize(self.__dimension)
        self.__arreglocanchas[self.__cantidad]=cancha
        self.__cantidad+=1
    
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\Recuperatorio 4\Canchas.csv")
            reader=csv.reader(archivo,delimiter=';')
            for fila in reader:
                self.agregarCancha(Cancha(fila[0],fila[1],int(fila[2])))
            archivo.close()
        except FileNotFoundError:
            print('Error al intentar abrir el archivo')
        except Exception as e:
            print('Error al intentar leer el archivo:',e)
            
    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__arreglocanchas[i])
            
    def buscarcancha(self,idcancha):
        i=0
        band=False
        while band is False and i<(self.__cantidad):
            if self.__arreglocanchas[i].getid()==idcancha:
                band=True
                return self.__arreglocanchas[i]
            else:
                i+=1
        if band is False:
            return None
    

# if __name__=="__main__":
#     gestor=Gestorcanchas()
#     gestor.cargarcsv()
#     gestor.mostrar()
            