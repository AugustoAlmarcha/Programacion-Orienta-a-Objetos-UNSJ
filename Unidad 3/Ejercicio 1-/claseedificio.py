from clasedepartamento import Departamento
class Edificio:
    __id: int
    __nombre: str
    __direccion: str
    __nombre_empresa: str
    __cantidad_pisos: int
    __cantidad_departamentos: int
    __listadepartamentos: list
    
    def __init__(self, id, nombre, direccion, nombre_empresa, cantidad_pisos, cantidad_departamentos):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__nombre_empresa = nombre_empresa
        self.__cantidad_pisos = cantidad_pisos
        self.__cantidad_departamentos = cantidad_departamentos
        self.__listadepartamentos = []
        
    def agregar_departamento(self, departamento):
        if isinstance(departamento, Departamento):
            self.__listadepartamentos.append(departamento)
    
    def mostrarpropietariosx(self):
        for departamento in self.__listadepartamentos:
            print(f"Propietario: {departamento.get_nombre_propietario()} del Departamento ID: {departamento.get_id()} en el Piso: {departamento.get_numero_piso()}")
    
    def contarsuperficie(self):
        superficietotal=0
        i=0
        while i < len(self.__listadepartamentos):
            superficietotal += self.__listadepartamentos[i].get_superficie_cubierta()
            i += 1
        return superficietotal
    
    def superficieespecifica(self, nombrepropietario):
        superficie=0
        i=0
        band=False
        while i < len(self.__listadepartamentos):
            if self.__listadepartamentos[i].get_nombre_propietario() == nombrepropietario:
                band = True
                superficie += self.__listadepartamentos[i].get_superficie_cubierta()
            i += 1
        if band is False:
            print("No se encontró el propietario con ese nombre.")
        return superficie
    
    def contarbañosdepartamento(self, numero):
        contador = 0
        i=0
        while i < len(self.__listadepartamentos):
            if self.__listadepartamentos[i].get_numero_piso() == numero and self.__listadepartamentos[i].get_cantidad_habitaciones() == 3 and self.__listadepartamentos[i].get_cantidad_banos() > 1:
                contador += 1
                print(f"Departamento ID: {self.__listadepartamentos[i].get_id()} en el Piso: {self.__listadepartamentos[i].get_numero_piso()} tiene 3 habitaciones y más de un baño.")
            i += 1
        return contador
            

    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_nombre_empresa(self):
        return self.__nombre_empresa
    
    def get_cantidad_pisos(self):
        return self.__cantidad_pisos
    
    def get_cantidad_departamentos(self):
        return self.__cantidad_departamentos
    
    def __str__(self):
        departamentos = "\n".join(str(dep) for dep in self.__listadepartamentos)
        return f"Edificio ID: {self.__id}, Nombre: {self.__nombre}, Dirección: {self.__direccion}, Empresa: {self.__nombre_empresa}, Pisos: {self.__cantidad_pisos}, Departamentos: {self.__cantidad_departamentos}, lista de departamentos:\n{departamentos}"