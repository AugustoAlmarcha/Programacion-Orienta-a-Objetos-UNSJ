from claseclientesnacionales import clientesNacionales
from Claseclienteslocales import ClientesLocales

class Nodo:
    __clientes = object
    __siguiente = object
    
    def __init__(self, clientes):
        self.__clientes = clientes
        self.__siguiente = None
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__clientes
    
    