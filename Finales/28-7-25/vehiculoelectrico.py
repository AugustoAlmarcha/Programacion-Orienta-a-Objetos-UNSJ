from clasevehiculo import Vehiculo
from clasebateria import Bateria
class VehiculoElectrico(Vehiculo):
    __autonomiaenkm:int
    __eficienciaporkm:float
    __listabateria:list

    def __init__(self, patente, capacidad, km, autonomiaenkm, eficienciaporkm):
        super().__init__(patente, capacidad, km)
        self.__autonomiaenkm = autonomiaenkm
        self.__eficienciaporkm = eficienciaporkm
        self.__listabateria = []

    def agregarbateria(self, bateria):
        if isinstance(bateria, Bateria):
            self.__listabateria.append(bateria)
        else:
            raise Exception("El objeto no es una instancia de Bateria")

    def getautonomiaenkm(self):
        return self.__autonomiaenkm
    
    def geteficienciaporkm(self):
        return self.__eficienciaporkm
    
    def __str__(self):
        baterias = ", \n".join([str(bateria) for bateria in self.__listabateria]) if self.__listabateria else "No hay baterias"
        return f"{super().__str__()}, Autonomía en km: {self.__autonomiaenkm}, Eficiencia por km: {self.__eficienciaporkm}, Baterías: \n {baterias}"

    def calculo(self):
        return self.__eficienciaporkm
    
    def listarvehiculosconenergia(self, distancia):
        i=0
        energiatotal=0
        band=False
        while i< len(self.__listabateria):
            energiatotal+= self.__listabateria[i].energiadisponible()
            i+=1
        if energiatotal >= distancia:
            print(f"El vehiculo con patente: {self.getpatente()} puede recorrer {distancia} km con la energia disponible.")
            band=True
        return band

    