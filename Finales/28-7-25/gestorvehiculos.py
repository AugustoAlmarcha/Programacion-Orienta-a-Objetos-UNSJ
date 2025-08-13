import csv
from clasevehiculo import Vehiculo
from clasecolectivo import Colectivo
from vehiculoelectrico import VehiculoElectrico
from clasebateria import Bateria
from clasenodo import *

class ListaVehiculos:
    __comienzo:Nodo
    __actual:Nodo
    __indice:int
    __tope:int
    
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato= self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def __getTope(self):
        return self.__tope
    
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\augus\Desktop\Final de Programacion a Objetos Almarcha Augusto 28-7-25\Vehiculos.csv")
            reader= csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                if fila[0] == "C":
                    self.agregar(Colectivo(fila[1], int(fila[2]), float(fila[3]), fila[4], int(fila[5]), fila[6]))
                elif fila[0] == "E":
                    vehiculox= VehiculoElectrico(fila[1], int(fila[2]), float(fila[3]), int(fila[4]), float(fila[5]))
                    self.agregar(vehiculox)
                    archivobaterias= open(r"C:\Users\augus\Desktop\Final de Programacion a Objetos Almarcha Augusto 28-7-25\Baterias.csv")
                    readerbaterias= csv.reader(archivobaterias,delimiter=';')
                    next(readerbaterias)
                    for fila2 in readerbaterias:
                        try:
                            if fila2[0] == vehiculox.getpatente():
                                vehiculox.agregarbateria(Bateria(fila2[0], int(fila2[1]), int(fila2[2])))
                        except Exception as e:
                            print("Error al agregar bateria:", e)
                    archivobaterias.close()
            archivo.close()
        except FileNotFoundError:
            print("El archivo CSV no se encontró.")
        except Exception as e:
            print("Error al leer el archivo CSV:", e)
      
    def agregar(self,vehiculo):
        nodo= Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
        print("Cargado Exitosamente!")
    
    def mostrar(self):
        if self.__comienzo is None:
            print("No hay vehiculos que mostrar.")
        else:
            actual = self.__comienzo
            while actual is not None:
                if isinstance(actual.getDato(), Colectivo):
                    print("Colectivo: ")
                elif isinstance(actual.getDato(), VehiculoElectrico):
                    print("Vehiculo Electrico: ")
                print(actual.getDato())
                actual = actual.getSiguiente()
                print("-------------------------")
    
    def listarvehiculoselectricos(self, distancia):
        if self.__comienzo is None:
            raise Exception("No hay vehículos eléctricos para listar.")
        actual = self.__comienzo
        while actual is not None:
            if isinstance(actual.getDato(), VehiculoElectrico):
                vehiculo = actual.getDato()
                bandera=vehiculo.listarvehiculosconenergia(distancia)
            actual = actual.getSiguiente()
        if bandera is False:
            print("No hay vehículos eléctricos que puedan recorrer la distancia especificada.")

    def mostrarespecifico(self):
        if self.__comienzo is None:
            raise Exception("No hay vehículos para mostrar.")
        actual = self.__comienzo
        while actual is not None:
            vehiculo = actual.getDato()
            print(f"Patente: {vehiculo.getpatente()}, Pasajeros: {vehiculo.getcapacidad()}, Tipo: {type(vehiculo).__name__}, Consumo: {vehiculo.consumo()}")
            actual = actual.getSiguiente()

    def agregarx(self, colectivo,posicion):
        if posicion < 0 or posicion > self.__tope:
            raise IndexError("Posición fuera de rango.")
        nodo = Nodo(colectivo)
        if posicion == 0:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
        else:
            actual = self.__comienzo
            while actual is not None and posicion > 1:
                actual = actual.getSiguiente()
                posicion -= 1
            if actual is None:
                raise IndexError("Posición fuera de rango.")
            nodo.setSiguiente(actual.getSiguiente())
            actual.setSiguiente(nodo)
        self.__tope += 1
        print("Colectivo agregado exitosamente en la posición indicada.")

# if __name__ == "__main__":
#     lista = ListaVehiculos()
#     lista.cargarcsv()
#     lista.mostrar()
                
