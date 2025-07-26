from clasemoto import *
import numpy as np
import csv
class GestorMoto:
    __arreglomoto:np.ndarray
    __cantidad:int
    __dimension:int
    __incremento:int
    
    def __init__(self):
        self.__cantidad=0
        self.__dimension=10
        self.__incremento=3
        self.__arreglomoto=np.zeros(self.__dimension,dtype=Moto)
        
    def agregarMoto(self,moto:Moto):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglomoto.resize(self.__dimension)
        self.__arreglomoto[self.__cantidad]=moto
        self.__cantidad+=1
        
    def cargarcsv(self):
        try:
            archivo = open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\Ejercicio 4\datosmoto.csv")
            reader= csv.reader(archivo, delimiter=";")
            next(reader)
            for fila in reader:
                self.agregarMoto(Moto(fila[0],fila[1],fila[2],int(fila[3])))
            archivo.close()
        except FileNotFoundError:
            print("El archivo no existe")
        except Exception as e:
            print(f"Error al leer el csv {e}")
    
    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__arreglomoto[i])
            
    def existe(self,patente):
        for i in range(self.__cantidad):
            if self.__arreglomoto[i].getpatente() == patente:
                return True
        return False
    
    def mostrardatos(self,patente):
        for i in range(self.__cantidad):
            if self.__arreglomoto[i].getpatente() == patente:
                print(self.__arreglomoto[i])
                return True
        return False
    
    def __iter__(self):
        return iter(self.__arreglomoto[:self.__cantidad])
    
    def buscarymostrar(self,i):
        while i<self.__cantidad:
            return self.__arreglomoto[i]
        
    
    

        
    

            
# if __name__=="__main__":
#     Motox=GestorMoto()
#     Motox.cargarcsv()
#     Motox.mostrar()
    
        
        
        
        
    