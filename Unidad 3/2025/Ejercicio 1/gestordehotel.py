from clasehabitacion import Habitacion
from clasehotel import Hotel
import csv

class GestorHotel:
    __listahotel:list
    
    def __init__(self):
        self.__listahotel = []
        
    def agregarHotel(self, hotel: Hotel):
        if isinstance(hotel, Hotel):
            self.__listahotel.append(hotel)
        else:
            raise TypeError("El objeto debe ser una instancia de la clase Hotel")
    
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 3\2025\Ejercicio 1\Hoteles.csv")
            reader = csv.reader(archivo , delimiter=';')
            for fila in reader:
                if len(fila[0]) > 5:
                    hotel= Hotel(fila[0], fila[1], fila[2])
                    self.agregarHotel(hotel)
                else:
                    hotel.agregarHabitacion(Habitacion(int(fila[0]), int(fila[1]), fila[2], float(fila[3]), fila[4].strip().lower() == 'true'))
            archivo.close()
        except FileNotFoundError:
            print("El archivo no se encontró.") 
        except Exception as e:
            print(f"Se produjo un error: {e}")
    
    def mostrar(self):
        for hotel in self.__listahotel:
            print(hotel)
            print("--------------------------------------------------")
    
    def agregarHabitacionx(self, nombre):
        i=0
        band=False
        while i < len(self.__listahotel) and band is False:
            if self.__listahotel[i].getNombre().lower() == nombre.lower():
                try:
                    self.__listahotel[i].agregardepartamento()
                except ValueError as e:
                    print(e)
                band = True
            i += 1
        if band is False:
            print("No se encontró el hotel con el nombre especificado.")
    
    def reservarhabitacion(self, numero, nombre):
        i=0
        band=False
        while i < len(self.__listahotel) and band is False:
            if self.__listahotel[i].getNombre().lower() == nombre.lower():
                self.__listahotel[i].reservarHabitacion(numero)
                band = True
            i += 1
        if band is False:
            print("No se encontró el hotel con el nombre especificado.")
    
    def liberarhabitacionx(self, numero, nombre):
        i=0
        band=False
        while i < len(self.__listahotel) and band is False:
            if self.__listahotel[i].getNombre().lower() == nombre.lower():
                self.__listahotel[i].liberarHabitacion(numero)
                band = True
            i += 1
        if band is False:
            print("No se encontró el hotel con el nombre especificado.")
            
    def mostrarHabitacionesPorTipo(self, tipo):
        i=0
        while i < len(self.__listahotel):
            print(f"Hotel: {self.__listahotel[i].getNombre()}")
            self.__listahotel[i].mostrarHabitacionesPorTipo(tipo)
            i += 1
    
    def habitacioneslibres(self):
        i=0
        while i < len(self.__listahotel):
            print(f"Hotel: {self.__listahotel[i].getNombre()}")
            self.__listahotel[i].habitacionesLibresPorPiso()
            i += 1
    
    def mostrardetallesx(self):
        i=0
        while i < len(self.__listahotel):
            print(f"Hotel: {self.__listahotel[i].getNombre()}")
            self.__listahotel[i].mostrardetallePorTipo()
            i += 1
        

        

    
    
# if __name__ == "__main__":
#     gestor = GestorHotel()
#     gestor.cargarcsv()
#     gestor.mostrar()
        
                
                
                