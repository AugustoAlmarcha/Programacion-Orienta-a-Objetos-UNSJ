from Claseclienteslocales import ClientesLocales

class clientesNacionales(ClientesLocales):
    __provincia:str
    __localidad:str
    __codigopostal:str
    
    def __init__(self,n,a,e,c,dp,t,provincia,localidad,codigopostal):
        super().__init__(n,a,e,c,dp,t)
        self.__provincia=provincia
        self.__localidad=localidad
        self.__codigopostal=codigopostal
        
    def getprovincia(self):
        return self.__provincia
    
    def getlocalidad(self):
        return self.__localidad
    
    def getcodigopostal(self):
        return self.__codigopostal
    
    def __str__(self):
        return super().__str__() + f"Provincia: {self.__provincia}, Localidad: {self.__localidad}, Codigo Postal: {self.__codigopostal}"
        