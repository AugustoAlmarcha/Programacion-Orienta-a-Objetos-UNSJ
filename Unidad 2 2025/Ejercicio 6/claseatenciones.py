class Atenciones:
    __dni: int
    __fechaatencion: str
    __importe: float
    
    def __init__(self, dni: int, fechaatencion: str, importe: float):
        self.__dni = dni
        self.__fechaatencion = fechaatencion
        self.__importe = importe
    
    def getDNI(self):
        return self.__dni
    
    def getFechaAtencion(self):
        return self.__fechaatencion
    
    def getImporte(self):
        return self.__importe
    
    def __str__(self):
        return f"DNI: {self.__dni}, Fecha de Atención: {self.__fechaatencion}, Importe: {self.__importe:.2f}"