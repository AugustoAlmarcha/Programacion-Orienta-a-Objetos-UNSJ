from clasecamiones import Camiones
from claseautomoviles import Automovil
from clasevehiculos import Vehiculo

class Gestorvehiculos:
    __listavehiculos:list
    
    def __init__(self):
        self.__listavehiculos = []
        
    def agregarvehiculo(self,vehiculo:Vehiculo):
        self.__listavehiculos.append(vehiculo)
    
    def mostrarvehiculos(self):
        if not self.__listavehiculos:
            print("No hay vehículos")
            return
        else:
            for vehiculo in self.__listavehiculos:
                if isinstance(vehiculo,Automovil):
                    print("Automovil")
                elif isinstance(vehiculo,Camiones):
                    print("Camion")
                print(vehiculo)
    
    def buscarvehiculo(self,matricula):
        i=0
        band=False
        while i<len(self.__listavehiculos) and not band:
            if self.__listavehiculos[i].getMatricula()==matricula:
                band=True
                if isinstance(self.__listavehiculos[i],Camiones):
                    print("Camion")
                elif isinstance(self.__listavehiculos[i],Automovil):
                    print("Automovil")
                print(self.__listavehiculos[i])
            i+=1
        if not band:
            raise Exception ("Vehículo no encontrado")
                
    def indicar(self):
        i=0
        while i<len(self.__listavehiculos):
            if isinstance(self.__listavehiculos[i],Camiones):
                print("Camion")
            elif isinstance(self.__listavehiculos[i],Automovil):
                print("Automovil")
            print(f"Matricula: {self.__listavehiculos[i].getMatricula()}, Modelo: {self.__listavehiculos[i].getmodelo()}, Costo total de alquiler del vehiculo: {self.__listavehiculos[i].alquiler()}")
            i+=1
            
# if __name__ == "__main__":
#     gestor = Gestorvehiculos()
#     gestor.mostrarvehiculos()