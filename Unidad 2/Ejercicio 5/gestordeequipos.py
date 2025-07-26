import csv
from claseequipo import *

class GestorEquipo:
    __listaequipos:list
    
    def __init__(self):
        self.__listaequipos = []
        
    def agregarEquipo(self, equipo:Equipo):
        self.__listaequipos.append(equipo)
        
    def cargarcsv(self):
        try:
            archivo= open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\Ejercicio 5\equipos2024.csv")
            reader= csv.reader(archivo, delimiter=";")
            next(reader)
            for fila in reader:
                self.agregarEquipo(Equipo(int(fila[0]),fila[1],int(fila[2]),int(fila[3]),int(fila[4]), int(fila[5])))
            archivo.close()
        except FileNotFoundError:
            print("El archivo no existe")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
    
    def mostrarEquipos(self):
        for equipo in self.__listaequipos:
            print(equipo)
        
    def ordenar(self):
        self.__listaequipos=sorted(self.__listaequipos,reverse=True)
    
    def actualizar(self,fechas):
        for equipo in self.__listaequipos:
            fechas.buscarid(equipo.getid())
            
    
        

# if __name__=="__main__":
#     gestor = GestorEquipo()
#     gestor.cargarcsv()
#     gestor.mostrarEquipos()
            
    