import csv 
from clasealquiler import *

class GestorAlquileres:
    __listaalquiler: list
    
    def __init__(self):
        self.__listaalquiler = []
        
    def agregarAlquiler(self, alquiler: Alquiler):
        self.__listaalquiler.append(alquiler)
        
    def cargarcsv(self):
        try:
            archivo = open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\Recuperatorio 4\Alquiler.csv")
            reader = csv.reader(archivo, delimiter = ';')
            for fila in reader:
                self.agregarAlquiler(Alquiler(fila[0], fila[1], (fila[2]), (fila[3]), int(fila[4])))
            archivo.close()
        except FileNotFoundError:
            print('Error al intentar abrir el archivo')
        except Exception as e:
            print('Error al intentar leer el archivo:', e)
            
    def mostrar(self):
        for alquiler in self.__listaalquiler:
            print(alquiler)
    
    def ordenar(self):
        self.__listaalquiler = sorted(self.__listaalquiler)
    
    def formato(self,canchas):
        i=0
        total=0
        while i<len(self.__listaalquiler):
            cancha=canchas.buscarcancha(self.__listaalquiler[i].getidcancha())    
            if cancha is not None:
                print(f"Hora:{self.__listaalquiler[i].gethora()}:{self.__listaalquiler[i].getminutos()} - Id de Cancha {self.__listaalquiler[i].getidcancha()} - Duracion del alquiler en horas:  {self.__listaalquiler[i].getduracion()/60} - Importe a pagar por hora:  {cancha.getimportexhora()}, Importe alquiler total:  {cancha.getimportexhora()*(self.__listaalquiler[i].getduracion()/60)}")
                total+=cancha.getimportexhora()*(self.__listaalquiler[i].getduracion()/60)
            else:
                print("No se encontro la cancha")
            i+=1
        print(f"Total recaudado {total}")
    
    def totalminutos(self):
        total=0
        id=input('Ingrese el identificador de la cancha que busca: ')
        for alquiler in self.__listaalquiler:
            if alquiler.getidcancha()==id:
                total+=alquiler.getduracion()
        print(f'La cancha {id} estuvo alquilada {total} minutos')
            
            
# if __name__ == "__main__":
#     gestor = GestorAlquileres()
#     gestor.cargarcsv()
#     gestor.mostrar()
#     gestor.ordenar()
#     print('Lista ordenada')
#     gestor.mostrar()