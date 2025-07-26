class Ruta:
    __codigo:int
    __destino:str
    __distanciatotalkm:float
    __rutaasignada:bool
    
    def __init__(self,codigo,destino,distancia,ruta):
        self.__codigo =codigo
        self.__destino = destino
        self.__distanciatotalkm = distancia
        self.__rutaasignada = ruta
        
    def __str__(self):
        return (f"Codigo: {self.__codigo}, Destino: {self.__destino}, Distancia Total {self.__distanciatotalkm}, Tiene ruta asignada? {self.__rutaasignada}")
    
    def get_codigo(self):
        return self.__codigo
    
    def get_destino(self):
        return self.__destino
    
    def get_distancia(self):
        return self.__distanciatotalkm
    
    def get_rutaasignada(self):
        return self.__rutaasignada
    
    def set_asignada(self, valor: bool):
        self.__rutaasignada = valor
    
    