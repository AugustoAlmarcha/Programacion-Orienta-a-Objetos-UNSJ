from clasepublicaciones import *
from claselibro import Libro
from claseCD import CD

class Nodo:
    __publicacion = object
    __siguiente = object
    
    def __init__(self, publicacion):
        self.__publicacion = publicacion
        self.__siguiente = None
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__publicacion