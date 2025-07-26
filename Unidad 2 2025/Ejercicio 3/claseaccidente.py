import numpy as np
class Accidente:
    __arreglo = np.ndarray
    
    def __init__(self):
        self.__arreglo = np.zeros([19, 12], dtype=int)
    
        
    def agregar_accidente(self):
        mes= int(input("Ingrese el mes del accidente (1-12): ")) - 1
        departamento = int(input("Ingrese el número del departamento (1-19): ")) - 1
        self.__arreglo[departamento][mes] += int(input("Ingrese la cantidad de accidentes: "))
        
    def mostrar_accidentes(self):
        print("Accidentes por departamento y mes:\n")
        print("Departamento")
        for i in range(19):
            print(f"{i+1}")
            for j in range(12):
                print(f"Mes {j + 1}: {self.__arreglo[i][j]} accidentes")
        
    def buscar(self,i,mesaccidente):
        return self.__arreglo[i][mesaccidente]
    
    def buscarmaximo(self,mesaccidente):
        i=0
        max=0
        while i<len(self.__arreglo):
            if self.__arreglo[i][mesaccidente] > max:
                print("entro")
                variable=i
            i+=1
        return variable
    
    def contar(self,numerox):
        i=0
        cuenta=0
        while i<len(self.__arreglo[numerox]):
            cuenta+=self.__arreglo[numerox][i]
            i+=1
        return cuenta
    
    def mostrar_accidentes_ordenados(self):
        print("Accidentes por departamento y mes:\n")
        
        # Encabezado
        print(f"{'Departamento':<15}", end='')
        for mes in range(1, 13):
            print(f"{mes:<5}", end='')  # Mes 1 a 12 con ancho fijo
        print()  # Salto de línea

        # Datos por departamento
        for i in range(19):
            print(f"{i+1:<15}", end='')  # Número del departamento
            for j in range(12):
                print(f"{self.__arreglo[i][j]:<5}", end='')  # Accidentes por mes
            print()  # Salto de línea por departamento

        # Fila de totales por mes
        print(f"{'TOTAL':<15}", end='')
        for mes in range(12):
            total_mes = 0
            for depto in range(19):
                total_mes += self.__arreglo[depto][mes]
            print(f"{total_mes:<5}", end='')
        print()
        
            
    
    