from clasepacientes import pacientes
import csv
class ManejadorPacientes:
    __listaPacientes: list
    
    def __init__(self):
        self.__listaPacientes = []
    
    def agregarPaciente(self, paciente: pacientes):
        self.__listaPacientes.append(paciente)
    
    def cargarcsv(self):
        try:
            archivo= open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\2025\Ejercicio 6\pacientes.csv")
            reader = csv.reader(archivo, delimiter=';')
            next(reader)
            for fila in reader:
                self.agregarPaciente(pacientes(int(fila[0]), fila[1], fila[2]))
            archivo.close()
        except FileNotFoundError:
            print("El archivo no se encuentra en la ruta especificada.")
        except Exception as e:
            print(f"Se produjo un error al cargar el archivo: {e}")
    
    def mostrarPacientes(self):
        for paciente in self.__listaPacientes:
            print(paciente)
    
    def pacientePorDNI(self, dni):
        i=0
        band=False
        while i < len(self.__listaPacientes) and band is False:
            if self.__listaPacientes[i].getDNI() == dni:
                band = True
            i += 1
        if band:
            return self.__listaPacientes[i-1].getNombre()
        else:
            print("No se encontró un paciente con ese DNI.")
            return None
    
    def pacientesSinAtencion(self, manejadorAtenciones):
        i=0
        band=False
        while i < len(self.__listaPacientes):
            if manejadorAtenciones.buscaratencion(self.__listaPacientes[i].getDNI()) is None:
                band = True
                print(f"Paciente sin atenciones: {self.__listaPacientes[i]}")
            i += 1    
    
    def ordenarPacientes(self):
        self.__listaPacientes= sorted(self.__listaPacientes)
    
# if __name__ == "__main__":
#     manejador = ManejadorPacientes()
#     manejador.cargarcsv()
#     manejador.mostrarPacientes()