from claseatenciones import Atenciones
import csv
import numpy as np
class ManejadorAtenciones:
    __arregloatenciones:np.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int
    
    def __init__(self):
        self.__dimension = 5
        self.__incremento = 5
        self.__cantidad = 0
        self.__arregloatenciones = np.empty(self.__dimension, dtype=Atenciones)
        
    def agregarAtencion(self, atencion: Atenciones):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloatenciones.resize(self.__dimension)
        self.__arregloatenciones[self.__cantidad] = atencion
        self.__cantidad += 1
        
    def cargarcsv(self):
        try:
            archivo = open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\2025\Ejercicio 6\atenciones.csv")
            reader = csv.reader(archivo, delimiter=';')
            next(reader)
            for fila in reader:
                self.agregarAtencion(Atenciones(int(fila[0]), fila[1], float(fila[2])))
            archivo.close()
        except FileNotFoundError:
            print("El archivo no se encuentra en la ruta especificada.")
        except Exception as e:
            print(f"Se produjo un error al cargar el archivo: {e}")
    
    def mostrarAtenciones(self):
        for i in range(self.__cantidad):
            print(self.__arregloatenciones[i])
            
    def atencionesPorFecha(self, fecha, manejadorPacientes):
        i=0
        band=False
        total=0
        while i < self.__cantidad:
            if self.__arregloatenciones[i].getFechaAtencion() == fecha:
                band = True
                pacientex= manejadorPacientes.pacientePorDNI(self.__arregloatenciones[i].getDNI())
                if pacientex is None:
                    print(f"No se encontró un paciente con DNI {self.__arregloatenciones[i].getDNI()}.")
                    i += 1
                else:
                    print(f"El dia {fecha} se atendio al paciente: {pacientex}")
                    total += self.__arregloatenciones[i].getImporte()
            i += 1
        if band:
            print(f"El importe total que debe disponer la UNSJ para el pago a la obra social en esa fecha es: {total:.2f}")
        else:
            print(f"No se encontraron atenciones para la fecha {fecha}.")
    
    def cantidadatenciones(self, dni, manejadorPacientes):
        i=0 
        band=False
        contador = 0
        pacientex= manejadorPacientes.pacientePorDNI(dni)
        if pacientex is None:
            print(f"No se encontró un paciente con DNI {dni}.")
        else:
            while i < self.__cantidad:
                if self.__arregloatenciones[i].getDNI() == dni:
                    band = True
                    contador += 1
                i += 1
            if band:
                print(f"El paciente {pacientex} tuvo {contador} atenciones.")
            else:
                print(f"El paciente {pacientex} no tuvo atenciones registradas.")
    
    def buscaratencion(self,dni):
        i = 0
        band = False
        while i < self.__cantidad and not band:
            if self.__arregloatenciones[i].getDNI() == dni:
                band = True
            i += 1
        if band:
            return self.__arregloatenciones[i-1]
        else:
            print(f"No se encontraron atenciones para el DNI {dni}.")
            return None
                
            
    
# if __name__ == "__main__":
#     manejador = ManejadorAtenciones()
#     manejador.cargarcsv()
#     manejador.mostrarAtenciones()