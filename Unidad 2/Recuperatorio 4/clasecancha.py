class Cancha:
    __id:str
    __tipodepiso:str
    __importexhora:int
    
    def __init__(self,id:str,tipodepiso:str,importexhora:int):
        self.__id=id
        self.__tipodepiso=tipodepiso
        self.__importexhora=importexhora
        
    def getid(self):
        return self.__id
    
    def gettipodepiso(self):
        return self.__tipodepiso
    
    def getimportexhora(self):
        return self.__importexhora
    
    def __str__(self):
        return f'{self.__id} - {self.__tipodepiso} - ${self.__importexhora}'