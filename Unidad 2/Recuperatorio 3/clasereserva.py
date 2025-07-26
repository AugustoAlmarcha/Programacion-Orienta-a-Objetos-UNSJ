class Reserva:
    __numerodereserva:int
    __nombreyapellido:str
    __cabañaasignada:int
    __fecha:str
    __cantidadhuespedes:int
    __cantidaddias:int
    __importedelaseña:int
    
    def __init__(self, numerodereserva:int, nombreyapellido:str, cabañaasignada:int, fecha:str, cantidadhuespedes:int, cantidaddias:int, importedelaseña:int):
        self.__numerodereserva = numerodereserva
        self.__nombreyapellido = nombreyapellido
        self.__cabañaasignada = cabañaasignada
        self.__fecha = fecha
        self.__cantidadhuespedes = cantidadhuespedes
        self.__cantidaddias = cantidaddias
        self.__importedelaseña = importedelaseña
        
    def getNumeroDeReserva(self):
        return self.__numerodereserva
    
    def getNombreYApellido(self):
        return self.__nombreyapellido
    
    def getCabañaAsignada(self):
        return self.__cabañaasignada
    
    def getFecha(self):
        return self.__fecha
    
    def getCantidadHuespedes(self):
        return self.__cantidadhuespedes
    
    def getCantidadDias(self):
        return self.__cantidaddias
    
    def getImporteDeLaSeña(self):
        return self.__importedelaseña
    
    def __str__(self):
        return f'Numero de Reserva: {self.__numerodereserva} - Nombre y Apellido: {self.__nombreyapellido} - Cabaña Asignada: {self.__cabañaasignada} - Fecha: {self.__fecha} - Cantidad de Huespedes: {self.__cantidadhuespedes} - Cantidad de Dias: {self.__cantidaddias} - Importe de la Seña: {self.__importedelaseña}'