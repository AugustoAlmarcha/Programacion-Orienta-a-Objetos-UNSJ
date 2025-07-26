class Facultad:
    __codigodefacu: int
    __nombre: str
    __direccion: str
    __Localidad: str
    __telefono: str
    
    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigodefacu = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__Localidad = localidad
        self.__telefono = telefono
        
    def __str__(self):
        return (f"Codigo de facultad: {self.__codigodefacu}, Nombre: {self.__nombre}, Direccion: {self.__direccion}, Localidad: {self.__Localidad}, Telefono: {self.__telefono}")
    
    def getcodigofacultad(self):
        return self.__codigodefacu
    
    def getnombre(self):
        return self.__nombre
    
    def getdireccion(self):
        return self.__direccion
    
    def getlocalidad(self):
        return self.__Localidad
    
    def gettelefono(self):
        return self.__telefono