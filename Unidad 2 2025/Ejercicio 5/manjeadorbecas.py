from clasebecas import Becas
import csv
import numpy as np

class ManejadorBecas:
    __arregloBecas: np.ndarray
    __dimension: int
    __cantidad: int
    __incremento: int
    
    def __init__ (self):
        self.__dimension = 10
        self.__cantidad = 0
        self.__incremento = 5
        self.__arregloBecas = np.empty(self.__dimension, dtype=Becas)
    
    def agregarBeca(self, beca):
        if self.__cantidad==self.__dimension:
            self.__dimension+= self.__incremento
            self.__arregloBecas.resize(self.__dimension)
        if isinstance(beca, Becas):
            self.__arregloBecas[self.__cantidad] = beca
            self.__cantidad += 1
    
    def cargarcsv(self):
        try:
            archivo = open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\2025\Ejercicio 5\becas.csv")
            reader = csv.reader(archivo, delimiter=";")
            next(reader)
            for fila in reader:
                self.agregarBeca(Becas(int(fila[0]), fila[1], float(fila[2])))
            archivo.close()
        except FileNotFoundError:
            print("El archivo no se encuentra en la ruta especificada.")
        except Exception as e:
            print(f"Se produjo un error al cargar el archivo: {e}")
    
    def mostrarBecas(self):
        for i in range(self.__cantidad):
            print(self.__arregloBecas[i])
    
    def getId(self, tipobeca):
        i=0 
        band=False
        while i < self.__cantidad and band is False:
            if self.__arregloBecas[i].getTipoBeca() == tipobeca:
                band = True
            else:
                i += 1
        if band:
            return self.__arregloBecas[i]
        else:
            print("No se encontró la beca con el tipo especificado.")
            return None
        
            
    
# if __name__ == "__main__":
#     manejador = ManejadorBecas()
#     manejador.cargarcsv()
#     manejador.mostrarBecas()
        

    
