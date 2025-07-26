from Clasepacientes import Paciente

class PacienteAmbulatorio(Paciente):
    __historialmedico:str
    __alergias:str
    __obrasocial:str
    
    def __init__(self,n,a,e,nt,historial,alergias,obrasocial):
        super().__init__(n,a,e,nt)
        self.__historialmedico=historial
        self.__alergias=alergias
        self.__obrasocial=obrasocial
        
    def getHistorial(self):
        return self.__historialmedico
    
    def getAlergias(self):
        return self.__alergias
    
    def getobrasocial(self):
        return self.__obrasocial
    
    def __str__(self):
        return super().__str__() + (f"Historial Medico: {self.__historialmedico}, Alergias: {self.__alergias}, Obra Social: {self.__obrasocial}, Precio Final {self.importeacobrar()}")
    
    def calculopaciente(self):
        valorconsulta= self.getvalorconsulta()
        if self.__obrasocial.strip().upper() == "OBRA SOCIAL PROVINCIA":
            return -valorconsulta + 5000
        elif self.__obrasocial.strip().upper() == "OSDE":
            return -valorconsulta + 2000
        else:
            return -valorconsulta + 10000
        