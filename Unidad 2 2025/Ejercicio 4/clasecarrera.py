class Carrera:
    __codigodecarrera:int
    __nombre:str
    __duracion:str
    __titulo:str
    __nivel:str
    __codigofacultad:int
    
    def __init__(self,codigo,nombre,duracion,titulo,nivel,codigofacu):
        self.__codigodecarrera=codigo
        self.__nombre=nombre
        self.__duracion=duracion
        self.__titulo=titulo
        self.__nivel=nivel
        self.__codigofacultad=codigofacu
    
    def __str__(self):
        return (f"Codigo de carrera {self.__codigodecarrera}, Nombre: {self.__nombre}, Duracion:{self.__duracion}, Titulo:{self.__titulo}, Nivel: {self.__nivel}, Codigo de facultad: {self.__codigofacultad}")
    
    def getcodigocarrera(self):
        return self.__codigodecarrera
    
    def getnombre(self):
        return self.__nombre
    
    def getduracion(self):
        return self.__duracion
    
    def gettitulo(self):
        return self.__titulo
    
    def getnivel(self):
        return self.__nivel
    
    def getcodigofacultad(self):
        return self.__codigofacultad
    
    def __lt__(self,otro):
        return self.__nombre < otro.getnombre()
    
    