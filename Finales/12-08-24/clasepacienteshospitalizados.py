from Clasepacientes import Paciente

class PacientesHospitalizados(Paciente):
    __numerohabitacion:int
    __fechaingreso:str
    __diagnostico:str
    __cantidaddiasinternacion:int
    __importeendescartables:float
    
    def __init__(self,n,a,e,nt,numerohabitacion,fechaingreso,diagnostico,cantidaddiasinternacion,descartables):
        super().__init__(n,a,e,nt)
        self.__numerohabitacion=numerohabitacion
        self.__fechaingreso=fechaingreso
        self.__diagnostico=diagnostico
        self.__cantidaddiasinternacion=cantidaddiasinternacion
        self.__importeendescartables=descartables
        
    def __str__(self):
        return super().__str__() + (f"Numero de Habitacion {self.__numerohabitacion}, Fecha de Ingreso: {self.__fechaingreso}, Diagnostico: {self.__diagnostico}, Cantidad dias de internacion: {self.__cantidaddiasinternacion}, importe en descartables: {self.__importeendescartables}, Precio Final {self.importeacobrar()}")
    
    def getnumerohabitacion(self):
        return self.__numerohabitacion
    
    def getfechaingreso(self):
        return self.__fechaingreso
    
    def getdiagnostico(self):
        return self.__diagnostico
    
    def getcantidaddiasinternacion(self):
        return self.__cantidaddiasinternacion
    
    def getimporteendescartables(self):
        return self.__importeendescartables
    
    def calculopaciente(self):
        return (self.__cantidaddiasinternacion * 150000) + self.__importeendescartables
    
    