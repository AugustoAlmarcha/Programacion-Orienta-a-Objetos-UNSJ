import csv
from clasenodo import Nodo
from Clasepacientes import Paciente
from clasepacientesambulatorios import PacienteAmbulatorio
from clasepacienteshospitalizados import PacientesHospitalizados

class ListaPacientes:
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
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Finales\12-08-24\pacientes.csv")
            reader= csv.reader(archivo,delimiter=',')
            for fila in reader:
                if fila[0] == "O":
                    self.agregaralfinal(PacienteAmbulatorio(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7]))
                elif fila[0] == "H":
                    self.agregaralfinal(PacientesHospitalizados(fila[1], fila[2], fila[3], fila[4], int(fila[5]), fila[6], fila[7], int(fila[8]), float(fila[9])))
            archivo.close()
        except FileNotFoundError:
            print("El archivo CSV no se encontró.")
        except Exception as e:
            print("Error al leer el archivo CSV:", e)
        
      
    def agregar(self,producto):
        nodo= Nodo(producto)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
        print("Cargado Exitosamente!")
    
    def mostrar(self):
        if self.__comienzo is None:
            print("No hay pacientes para mostrar.")
        else:
            actual = self.__comienzo
            while actual is not None:
                if isinstance(actual.getDato(), PacienteAmbulatorio):
                    print("Paciente Ambulatorio:")
                elif isinstance(actual.getDato(), PacientesHospitalizados):
                    print("Pacientes Hospitalizados:")
                print(actual.getDato())
                actual = actual.getSiguiente()
                print("-------------------------")
                
    def agregaralfinal(self, uncliente):
        nuevoNodo = Nodo(uncliente)
        if self.__comienzo is None:
            self.__comienzo = nuevoNodo
        else:
            aux = self.__comienzo
            while aux.getSiguiente() is not None:
                aux = aux.getSiguiente()
            aux.setSiguiente(nuevoNodo)
        self.__actual = self.__comienzo
        self.__tope += 1
        print("Agregado exitosamente!\n")
        
    def cantidad(self):
        contambulatorio=0
        conthospitalizado=0
        aux=self.__comienzo
        while aux is not None:
            if isinstance(aux.getDato(), PacienteAmbulatorio):
                contambulatorio+=1
            elif isinstance(aux.getDato(), PacientesHospitalizados) and aux.getDato().getdiagnostico().strip().lower() == "neumonia":
                conthospitalizado +=1
            aux = aux.getSiguiente()
        print(f"La cantidad de pacientes ambulatorios que posee el hospital es de {contambulatorio} y la cantidad de pacientes hospitalizados con neumonia es de {conthospitalizado}")
            
    def mostrartodoslosimportes(self):
        aux=self.__comienzo
        while aux is not None:
            print(f"El paciente llamado {aux.getDato().getnombre()} {aux.getDato().getapellido()} pago {aux.getDato().importeacobrar()}")
            aux=aux.getSiguiente()
            
    def clienteenposicion(self,posicion):
        if self.__comienzo is None:
            print("No hay clientes para mostrar")
        else:
            i=0
            actual=self.__comienzo
            while i < posicion and actual is not None:
                actual = actual.getSiguiente()
                i+=1
            if actual is not None:
                if isinstance(actual.getDato(), PacienteAmbulatorio):
                    print(f"En la posicion {posicion} se encuentra un Paciente Ambulatorio")
                elif isinstance(actual.getDato(), PacientesHospitalizados):
                    print(f"En la posicion {posicion} se encuentra un Paciente hospitalizado")
            else:
                raise IndexError
            
        
                
                
# if __name__ == "__main__":
#     lista = ListaPacientes()
#     lista.cargarcsv()
#     lista.mostrar()


