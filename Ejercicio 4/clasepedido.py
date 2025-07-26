class Pedido:
    __patente:str
    __idpedido:int
    __comidas:str
    __tiempoestimado:float
    __tiemporeal:float
    __precio:float
    
    def __init__(self,patente,id,comidas,tiempoestimado,precio,tr=0):
        self.__patente=patente
        self.__idpedido=id
        self.__comidas=comidas
        self.__tiempoestimado=tiempoestimado
        self.__precio=precio
        self.__tiemporeal=tr  
    
    def getpatente(self):
        return self.__patente
    
    def getidpedido(self):
        return self.__idpedido
    
    def getcomida(self):
        return self.__comidas
    
    def gettiemporeal(self):
        return self.__tiemporeal
    
    def gettiempoestimado(self):
        return self.__tiempoestimado
    
    def getprecio(self):
        return self.__precio
    
    def settiemporeal(self,tiemporeal):
        self.__tiemporeal=tiemporeal
    
    def __str__(self):
        return(f"Patente:{self.__patente}, Id del pedido:{self.__idpedido}, Comida:{self.__comidas},Tiempo estimado:{self.__tiempoestimado},Tiempo real:{self.__tiemporeal}, Precio:{self.__precio}")
        
    def __lt__(self,otro):
        return self.__patente < otro.getpatente()