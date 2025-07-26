class Departamentos:
    numero: int
    nombre: str
    
    def __init__(self, numero: int, nombre: str):
        self.numero = numero
        self.nombre = nombre
        
    def __str__(self):
        return f"Departamento {self.numero}: {self.nombre}"
    
    def getnumero(self):
        return self.numero
    
    def getnombre(self):
        return self.nombre
    
    