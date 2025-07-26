from claseclientesnacionales import clientesNacionales
from Claseclienteslocales import ClientesLocales
from clasenodo import Nodo

class ListaClientes:
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
    
    def agregar(self,clientes):
        nodo= Nodo(clientes)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
        print("Cargado Exitosamente!")
        
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
        
    def mostrar(self):
        if self.__comienzo is None:
            print("No hay clientes para mostrar.")
        else:
            actual = self.__comienzo
            while actual is not None:
                if isinstance(actual.getDato(), clientesNacionales):
                    print("Cliente Nacional")
                elif isinstance(actual.getDato(), ClientesLocales):
                    print("Cliente Local")
                print(actual.getDato())
                actual = actual.getSiguiente()
                print("-------------------------")
        
    def esclientenacional(self):
        if self.__comienzo is None:
            print("No hay clientes para mostrar")
        else:
            actual=self.__comienzo
            while actual is not None:
                if isinstance(actual.getDato(), clientesNacionales):
                    print(f"Cliente Nacional: Nombre: {actual.getDato().getnombre()} Provincia: {actual.getDato().getprovincia()}")
                actual = actual.getSiguiente()
                print("-------------------")
    
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
                if isinstance(actual.getDato(), clientesNacionales):
                    print(f"En la posicion {posicion} se encuentra un cliente Nacional")
                elif isinstance(actual.getDato(), ClientesLocales):
                    print(f"En la posicion {posicion} se encuentra un cliente Local")
            else:
                print("Posicion no encontrada")
                
            
        
    

