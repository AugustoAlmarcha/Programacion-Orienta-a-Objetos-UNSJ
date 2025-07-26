import csv
from claseladrillo import Ladrillo
from clasegestormaterial import ClaseGestorMaterial
from random import randint

class GestorLadrillos:
    __listaladrillos: list
    
    def __init__(self):
        self.__listaladrillos = []
        
    def agregarLadrillo(self, ladrillo: Ladrillo):
        self.__listaladrillos.append(ladrillo)

    def cargarcsv(self, gestormaterial):
        try:
            archivo = open(r"Ejercicios 2da chance/Unidad 3/Ejercicio 2/ladrillos.csv")
            reader = csv.reader(archivo, delimiter=';')
            next(reader)  
            for fila in reader:
                l = Ladrillo(int(int(fila[0])), int(fila[1]), float(fila[2]), float(fila[3]))
                if randint(0, 1) == 1:
                    material = gestormaterial.get_material_random()
                    if material is not None:
                        l.agregarMaterial(material)
                self.agregarLadrillo(l)
            archivo.close()
        except FileNotFoundError:
            print("El archivo no se encuentra en la ruta especificada.")
        except Exception as e:
            print(f"Se produjo un error al cargar el archivo: {e}")
    
    def mostrarladrillos(self):
        for ladrillo in self.__listaladrillos:
            print(ladrillo)
            
    def costomaterial(self, idladrillo):
        i=0
        band=False
        while band is False and i < len(self.__listaladrillos):
            if self.__listaladrillos[i].getId()== idladrillo:
                band = True
                self.__listaladrillos[i].mostrar_materiales()
            i += 1
        if band is False:
            print("No se encontró el ladrillo con el ID especificado.")
            
    def mostrarcostototal(self):
        i=0
        while i < len(self.__listaladrillos):
            print(f"Ladrillo ID: {self.__listaladrillos[i].getId()}, Costo Total: ${self.__listaladrillos[i].calcularCosto()}")
            i += 1

    def mostrarmaterialesdelladrillo(self):
        i=0
        band=False
        while i<len(self.__listaladrillos):
            self.__listaladrillos[i].mostrardetalle()
            i += 1
    
   
                
                
                
                    
                    
    
# if __name__ == "__main__":
#     gestormaterial = ClaseGestorMaterial()
#     gestormaterial.cargarcsv()
#     gestormaterial.mostrarmaterial()

#     gestorladrillos = GestorLadrillos()
#     gestorladrillos.cargarcsv(gestormaterial)
#     gestorladrillos.mostrarladrillos()
