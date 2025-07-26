import csv
import numpy as np
from clasemiembro import *

class GestorMiembro:
    __arreglomiembro:np.ndarray
    __dimension:int
    __cantidad:int
    __incremento:int
    
    def __init__(self):
        self.__dimension=10
        self.__arreglomiembro=np.empty(self.__dimension,dtype=Miembro)
        self.__cantidad=0
        self.__incremento=5
        
    def agregarMiembro(self,miembro:Miembro):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglomiembro.resize(self.__dimension)
        self.__arreglomiembro[self.__cantidad]=miembro
        self.__cantidad+=1
    
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\Recuperatorio 2\Miembros.csv")
            reader=csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                self.agregarMiembro(Miembro(int(fila[0]),fila[1],fila[2]))
            archivo.close()
        except FileNotFoundError:
            print("No se pudo abrir el archivo")
        except Exception as e:
            print(e)
            
    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__arreglomiembro[i])
            
    def buscarmiembro(self,correo):
        i=0
        band=False
        while i<self.__cantidad and band is False:
            if self.__arreglomiembro[i].getCorreo()==correo:
                band=True
                return self.__arreglomiembro[i].getID()
            i+=1
        if band==False:
            return None
        
    def buscarporid(self,id):
        i=0
        band=False
        while i<self.__cantidad and band is False:
            if self.__arreglomiembro[i].getID()==id:
                band=True
                return self.__arreglomiembro[i]
            i+=1
        if band==False:
            return None
    
    
            
            
                
            
# if __name__ == '__main__':
#     gm=GestorMiembro()
#     gm.cargarcsv()
#     gm.mostrar()
    
                