from claselibro import Libro
class Biblioteca:
    __nombre:str
    __direccion:str
    __telefono:str
    __libros:list
    
    def __init__(self, nombre:str, direccion:str, telefono:str):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__libros = []
        
    def agregar_libro(self, libro:Libro):
        self.__libros.append(libro)
        
    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_telefono(self):
        return self.__telefono
    
    def __str__(self):
        libros = ', '.join([str(libro) for libro in self.__libros]) if self.__libros else "No hay libros"
        return f"Biblioteca: {self.__nombre}, Dirección: {self.__direccion}, Teléfono: {self.__telefono}, Libros: {libros}"
    
    def agregarnuevolibro(self, libro:Libro):
        i=0
        band=False
        while i < len(self.__libros) and not band:
            if self.__libros[i].get_titulo() == libro.get_titulo():
                print("El libro ya existe en la biblioteca.")
                band = True
            i += 1
        if not band:
            self.agregar_libro(libro)
            print(f"Libro '{libro.get_titulo()}' agregado a la biblioteca '{self.__nombre}'.")
    
    def eliminar(self,libro):
        i=0
        band=False
        while i< len(self.__libros) and band is False:
            if self.__libros[i].get_titulo() == libro:
                band=True
                self.__libros.pop(i)
                print(f"El Libro {libro} fue eliminado correctamente")
            i+=1
        if band is False:
            print("No se encontro el libro que busca")
    
    def buscar(self,libro):
        i=0
        band=False
        while i< len(self.__libros) and band is False:
            if self.__libros[i].get_titulo().lower() == libro:
                band=True
            else:
                i+=1
        if band is True:
            return self.__libros[i]
        else:
            print(f"No se encontro el libro en {self.get_nombre()}")
            return None
    
    def listar(self):
        for libro in self.__libros:
            print(libro.get_titulo())
                
            
            