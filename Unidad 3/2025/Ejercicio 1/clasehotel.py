from clasehabitacion import Habitacion
class Hotel:
    __nombre : str
    __direccion : str
    __telefono : str
    __listaHabitaciones : list
    
    def __init__(self, nombre: str, direccion: str, telefono: str):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__listaHabitaciones = []
        
    def agregarHabitacion(self, habitacion):
        if isinstance(habitacion, Habitacion):
            self.__listaHabitaciones.append(habitacion)
        else:
            raise TypeError("El objeto debe ser una instancia de la clase Habitacion")
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def __str__(self):
        habitaciones_str = ', '.join(str(h) for h in self.__listaHabitaciones)
        return f"Hotel: {self.__nombre}, Dirección: {self.__direccion}, Teléfono: {self.__telefono}, Habitaciones: {habitaciones_str}"
    
    def agregardepartamento(self):
        numero = int(input("Ingrese el número del departamento: "))
        piso = int(input("Ingrese el piso del departamento: "))
        for habitacion in self.__listaHabitaciones:
            if habitacion.getNumero() == numero and habitacion.getPiso() == piso:
                raise ValueError(f"Ya existe una habitación con número {numero} y piso {piso}.")
        tipo = input("Ingrese el tipo de departamento (sencillo, doble, suite): ")
        precio = float(input("Ingrese el precio por noche: "))
        disponible = input("¿Está disponible? (si/no): ").strip().lower() == 'si'
        self.__listaHabitaciones.append(Habitacion(numero, piso, tipo, precio, disponible))
        
    def reservarHabitacion(self,numero):
        i=0
        band=False
        while i < len(self.__listaHabitaciones) and band is False:
            if self.__listaHabitaciones[i].getNumero() == numero:
                if self.__listaHabitaciones[i].getDisponible():
                    self.__listaHabitaciones[i].setDisponible(False)
                    print(f"Reserva exitosa para la habitación {numero}.")
                else:
                    print(f"La habitación {numero} no está disponible.")
                band = True
            i += 1
        if band is False:
            print(f"La habitación {numero} no existe.")
    
    def liberarHabitacion(self,numero):
        i=0
        band=False
        while i < len(self.__listaHabitaciones) and band is False:
            if self.__listaHabitaciones[i].getNumero() == numero:
                if not self.__listaHabitaciones[i].getDisponible():
                    self.__listaHabitaciones[i].setDisponible(True)
                    print(f"La habitación {numero} ha sido liberada.")
                else:
                    print(f"La habitación {numero} ya estaba disponible.")
                band = True
            i += 1
        if band is False:
            print(f"La habitación {numero} no existe.")
            
    def mostrarHabitacionesPorTipo(self, tipo):
        i=0
        band = False
        while i < len(self.__listaHabitaciones):
            if self.__listaHabitaciones[i].getTipoDeHabitacion().lower() == tipo.lower():
                print(f"Numero: {self.__listaHabitaciones[i].getNumero()}, Piso: {self.__listaHabitaciones[i].getPiso()}")
                band = True
            i += 1
        if not band:
            print(f"No hay habitaciones del tipo {tipo} en el hotel {self.__nombre}.")
            
    def habitacionesLibresPorPiso(self):
        i=0
        while i < len(self.__listaHabitaciones):
            cont=0
            piso = self.__listaHabitaciones[i].getPiso()
            while i < len(self.__listaHabitaciones) and self.__listaHabitaciones[i].getPiso() == piso:
                if self.__listaHabitaciones[i].getDisponible():
                    cont += 1
                i += 1
            print(f"En el piso {piso} hay {cont} habitaciones libres.")
    
    def mostrardetallePorTipo(self):
        i = 0
        tipos_vistos = set()
        while i < len(self.__listaHabitaciones):
            tipo = self.__listaHabitaciones[i].getTipoDeHabitacion()
            if tipo not in tipos_vistos:
                print(f"Tipo de habitación: {tipo}")
                print(f"{'Número':<15} {'Piso':<10} {'Precio':<10} {'Disponibilidad'}")
                j = 0
                while j < len(self.__listaHabitaciones):
                    hab = self.__listaHabitaciones[j]
                    if hab.getTipoDeHabitacion() == tipo:
                        print(f"{hab.getNumero():<15} {hab.getPiso():<10} {hab.getPrecio():<10} {hab.getDisponible()}")
                    j += 1
                print() 
                tipos_vistos.add(tipo)
            i += 1
                