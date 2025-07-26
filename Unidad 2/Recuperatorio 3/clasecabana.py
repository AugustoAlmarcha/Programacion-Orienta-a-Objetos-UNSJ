class Cabaña:
    __numero:int
    __canthabitaciones:int
    __cantidadcamasgrandes:int
    __cantidadcamaschicas:int
    __importepordia:int
    
    def __init__(self, numero:int, canthabitaciones:int, cantidadcamasgrandes:int, cantidadcamaschicas:int, importepordia:int):
        self.__numero = numero
        self.__canthabitaciones = canthabitaciones
        self.__cantidadcamasgrandes = cantidadcamasgrandes
        self.__cantidadcamaschicas = cantidadcamaschicas
        self.__importepordia = importepordia
        
    
    def getNumero(self):
        return self.__numero
    
    def getImportePorDia(self):
        return self.__importepordia
    
    def getCanHabitaciones(self):
        return self.__canthabitaciones
    
    def getCanCamasGrandes(self):
        return self.__cantidadcamasgrandes
    
    def getCanCamasChicas(self):
        return self.__cantidadcamaschicas
    
    def __str__(self):
        return f'Numero: {self.__numero} - Habitaciones: {self.__canthabitaciones} - Camas Grandes: {self.__cantidadcamasgrandes} - Camas Chicas: {self.__cantidadcamaschicas} - Importe por dia: {self.__importepordia}'
    
    def __ge__(self, cantidadpersonas):
        capacidad= (self.__cantidadcamasgrandes * 2) + self.__cantidadcamaschicas
        return capacidad >= cantidadpersonas
    