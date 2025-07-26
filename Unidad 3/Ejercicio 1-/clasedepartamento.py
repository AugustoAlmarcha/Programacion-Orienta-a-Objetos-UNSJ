class Departamento:
    __id: int
    __nyapropietario: str
    __numeropiso: int
    __numerodepartamento: int
    __cantidadhabitaciones: int
    __cantidadbanos: int
    __superficiecubierta: float
    
    def __init__(self, id, nyapropietario, numeropiso, numerodepartamento, cantidadhabitaciones, cantidadbanos, superficiecubierta):
        self.__id = id
        self.__nyapropietario = nyapropietario
        self.__numeropiso = numeropiso
        self.__numerodepartamento = numerodepartamento
        self.__cantidadhabitaciones = cantidadhabitaciones
        self.__cantidadbanos = cantidadbanos
        self.__superficiecubierta = superficiecubierta

    def get_id(self):
        return self.__id

    def get_nombre_propietario(self):
        return self.__nyapropietario

    def get_numero_piso(self):
        return self.__numeropiso

    def get_numero_departamento(self):
        return self.__numerodepartamento

    def get_cantidad_habitaciones(self):
        return self.__cantidadhabitaciones

    def get_cantidad_banos(self):
        return self.__cantidadbanos

    def get_superficie_cubierta(self):
        return self.__superficiecubierta

    def __str__(self):
        return f"Departamento ID: {self.__id}, Propietario: {self.__nyapropietario}, Piso: {self.__numeropiso}, Departamento: {self.__numerodepartamento}, Habitaciones: {self.__cantidadhabitaciones}, Baños: {self.__cantidadbanos}, Superficie Cubierta: {self.__superficiecubierta}"