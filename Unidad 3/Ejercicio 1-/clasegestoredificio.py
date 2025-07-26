import csv
from claseedificio import Edificio
from clasedepartamento import Departamento

class GestorEdificio:
    __edificio: list
    
    def __init__(self):
        self.__edificio = []
    
    def agregaredifcio(self,edificio: Edificio):
        if isinstance(edificio, Edificio):
            self.__edificio.append(edificio)
   
    def cargarcsv(self):
        try:
            archivo = open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 3\Ejercicio 1\EdificioNorte.csv")
            reader = csv.reader(archivo, delimiter=';')
            idx=0
            for fila in reader:
                if idx != fila[0]:
                    idx = fila[0]
                    e= Edificio(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
                    self.agregaredifcio(e)
                else:
                    e.agregar_departamento(Departamento(int(fila[1]), fila[2], int(fila[3]), int(fila[4]), int(fila[5]), int(fila[6]), float(fila[7])))
            archivo.close()
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
    
    def mostrar(self):
        for edificio in self.__edificio:
            print(edificio)
    
    def mostrarpropietarios(self, nombre):
        i=0
        band= False
        while band is False and i < len(self.__edificio):
            if self.__edificio[i].get_nombre() == nombre:
                band = True
                self.__edificio[i].mostrarpropietariosx()
            i += 1
        if band is False:
            print("No se encontró el edificio con ese nombre.")
    
    def superficietotalx(self, nombre):
        i=0
        band= False
        superficie = 0
        while band is False and i < len(self.__edificio):
            if self.__edificio[i].get_nombre() == nombre:
                band = True
                superficie=self.__edificio[i].contarsuperficie()
                print(f"La superficie total cubierta del edificio {nombre} es: {superficie} m²")
            i += 1
        if band is False:
            print("No se encontró el edificio con ese nombre.")
            
    def superficie(self, nombrepropietario):
        i=0
        band= False
        superficiex = 0
        while band is False and i < len(self.__edificio):
            superficiex = self.__edificio[i].superficieespecifica(nombrepropietario)
            if superficiex != 0:
                band = True
                total = self.__edificio[i].contarsuperficie()
                porcentaje = (superficiex / total) * 100
                print(f"La superficie cubierta del departamento de {nombrepropietario} es: {superficiex} m², lo que representa el {porcentaje:.2f}% del total del edificio {self.__edificio[i].get_nombre()}.")
            i += 1
        if band is False:
            print("No se encontró el propietario con ese nombre.")
    
    def contar(self, numero):
        i=0
        band= False
        contador = 0
        while band is False and i < len(self.__edificio):
            contador = self.__edificio[i].contarbañosdepartamento(numero)
            if contador != 0:
                band = True
                print(f"En el piso {numero} hay {contador} departamentos con 3 habitaciones y más de un baño.")
            i += 1
        if band is False:
            print("No se encontró el piso con ese número.")
            
# if __name__ == "__main__":
#     gestor = GestorEdificio()
#     gestor.cargarcsv()
#     gestor.mostrar()
                    
                    
                    

                
    
    
    