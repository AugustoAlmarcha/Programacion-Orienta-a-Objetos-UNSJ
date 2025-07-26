import csv 
import numpy as np
from clasecabana import *

class GestorCabanas:
    __arreglocabanas:np.ndarray
    __cantidad:int
    __dimension:int
    __incremento:int
    
    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 10
        self.__incremento = 5
        self.__arreglocabanas = np.empty(self.__dimension, dtype = Cabaña)
        
    def agregarCabana(self, cabana:Cabaña):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglocabanas.resize(self.__dimension)
        self.__arreglocabanas[self.__cantidad] = cabana
        self.__cantidad += 1
        
    def cargarcsv(self):
        try:
            archivo = open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\Recuperatorio 3\Cabañas.csv")
            reader = csv.reader(archivo, delimiter = ';')
            next(reader)
            for fila in reader:
                self.agregarCabana(Cabaña(int(fila[0]), int(fila[1]), int(fila[2]), int(fila[3]), int(fila[4])))
            archivo.close()
        except Exception as e:
            print(f'Error al cargar el archivo: {e}')
        except FileNotFoundError:
            print('No se encontro el archivo')
    
    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__arreglocabanas[i])
    
    def buscarCabana(self, reserva):
        huespedes = int(input('Ingrese la cantidad de huespedes: '))
        i=0
        band=False
        cont=0
        while i < self.__cantidad:
            reservada = reserva.estareservada(self.__arreglocabanas[i].getNumero())
            if self.__arreglocabanas[i] >= huespedes and reservada is False:
                print("Cabaña disponible: ", self.__arreglocabanas[i].getNumero())
                band=True
                cont+=1
            i+=1
        if band:
            print(f'Hay {cont} cabañas disponibles')
        else:
            print('No hay cabañas disponibles')
            
    def ImportePorDia(self, numero):
        i=0
        band=False
        while i < self.__cantidad and band is False:
            if self.__arreglocabanas[i].getNumero() == numero:
                band=True
            i+=1
        if band:
            return self.__arreglocabanas[i-1].getImportePorDia()
        else:
            return None
            
        
            
# if __name__ == '__main__':
#     gestor=GestorCabanas()
#     gestor.cargarcsv()
#     gestor.mostrar()
#     gestor.buscarCabana()

            