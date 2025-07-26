class ClientesLocales():
    __nombre:str
    __apellido:str
    __email:str
    __contraseña:str
    __direccionpostal:str
    __telefono:str
    
    def __init__(self,nombre,apellido,email,contraseña,direccion,telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email=email
        self.__contraseña = contraseña
        self.__direccionpostal = direccion
        self.__telefono = telefono
        
    def getnombre(self):
        return self.__nombre
    
    def getapellido(self):
        return self.__apellido
    
    def getemail(self):
        return self.__email
    
    def getcontraseña(self):
        return self.__contraseña
    
    def getdireccionpostal(self):
        return self.__direccionpostal
    
    def gettelefono(self):
        return self.__telefono
    
    def __str__(self):
        return f"Nombre: {self.__nombre},Apellido: {self.__apellido}, Email:{self.__email}, Contraseña: {self.__contraseña}, Direccion: {self.__direccionpostal}, Telefono{self.__telefono}"
    
    
    