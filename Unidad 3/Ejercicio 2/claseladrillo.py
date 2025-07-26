from clasematerialrefractario import MaterialRefractario
class Ladrillo:
    __alto:int
    __largo:int
    __ancho:int
    __cantidad:int
    __id:int
    __kgmateriaprima:float
    __costo:float
    __listamaterial: list

    def __init__(self, cantidad, id, kgmateriaprima, costo):
        self.__cantidad = cantidad
        self.__id = id
        self.__kgmateriaprima = kgmateriaprima
        self.__costo = costo
        self.__listamaterial = []
        self.__alto = 7
        self.__largo = 25
        self.__ancho = 15
    
    def agregarMaterial(self, material: MaterialRefractario):
        self.__listamaterial.append(material)
    
    def mostrar_materiales(self):
        if len(self.__listamaterial) == 0:
            print("No tiene materiales.")
        else:
            for material in self.__listamaterial:
                print(f"Característica: {material.getCaracteristicas()}, Costo adicional: ${material.getCostoAdicional()}")
    
    def calcularCosto(self):
        total_costo = self.__costo
        for material in self.__listamaterial:
            total_costo += material.getCostoAdicional() * material.getCantidadUtilizada()
        return total_costo
    

    def mostrardetalle(self):
        # Imprimir encabezado siempre
        print(f"{'N° Identificador':<15} {'Material':<30} {'Costo Asociado':>15}")
        
        if len(self.__listamaterial) == 0:
            print(f"{self.__id:<15} {'No tiene materiales.':<30} {'':>15}")
        else:
            for material in self.__listamaterial:
                costo_asociado = material.getCostoAdicional() * material.getCantidadUtilizada()
                print(f"{self.__id:<15} {material.getCaracteristicas():<30} ${costo_asociado:>14.2f}")


    def getId(self):
        return self.__id
    
    def getAlto(self):
        return self.__alto
    
    def getLargo(self):
        return self.__largo
    
    def getAncho(self):
        return self.__ancho
    
    def getCantidad(self):
        return self.__cantidad
    
    def getKgMateriaPrima(self):
        return self.__kgmateriaprima
    
    def getCosto(self):
        return self.__costo
    
    def getListamaterial(self):
        return self.__listamaterial
    
    def __str__(self):
        if self.__listamaterial:
            materiales_str = ', '.join(str(material) for material in self.__listamaterial)
        else:
            materiales_str = 'Sin materiales'
        return f"ID: {self.__id}, Alto: {self.__alto}, Largo: {self.__largo}, Ancho: {self.__ancho}, Cantidad: {self.__cantidad}, Kg Materia Prima: {self.__kgmateriaprima}, Costo: {self.__costo}, Materiales: {materiales_str}"