from clasemedio import Medio
from claseprograma import Programa
class Radio(Medio):
    __frecuencia:str
    __listaprogramas:list
    
    def __init__(self,nombre,audiencia,frecuencia):
        super().__init__(nombre,audiencia)
        self.__frecuencia = frecuencia
        self.__listaprogramas = []
        
    def get_frecuencia(self):
        return self.__frecuencia
    
    def Eslafrecuencia(self,frecuencia):
        return self.__frecuencia == frecuencia
        
    def agregarprograma(self,programa):
        self.__listaprogramas.append(programa)
    
    def __str__(self):
        programas= ', \n'.join([str(programa) for programa in self.__listaprogramas]) if self.__listaprogramas else "No hay programas"
        return super().__str__() + (f"Frecuencia: {self.__frecuencia},Programas:\n {programas}")
    
    def calculo(self):
        return len(self.__listaprogramas)

    def programaexiste(self,nombre):
        i=0
        band=False
        while i<len(self.__listaprogramas) and not band:
            if self.__listaprogramas[i].getNombre()==nombre:
                band=True
                print(f"El programa {nombre} se emite en {self.get_nombre()}, en la frecuencia {self.get_frecuencia()} y empieza a transmitirse a las {self.__listaprogramas[i].getHorainicio()}")
            i+=1
        if band is False:
            raise ValueError