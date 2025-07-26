from clasebeneficiarios import Beneficiarios
import csv
class ManejadorBeneficiarios:
    __listaBeneficiarios: list
    
    def __init__(self):
        self.__listaBeneficiarios = []
    
    def agregarBeneficiario(self,beneficiario):
        if isinstance(beneficiario, Beneficiarios):
            self.__listaBeneficiarios.append(beneficiario)
    
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\2025\Ejercicio 5\beneficiarios.csv")
            reader=csv.reader(archivo,delimiter=";")
            next(reader)
            for fila in reader:
                self.agregarBeneficiario(Beneficiarios(int(fila[0]),fila[1],fila[2],fila[3],fila[4],int(fila[5]),int(fila[6]),int(fila[7])))
            archivo.close()
        except FileNotFoundError:
            print("El archivo no se encuentra en la ruta especificada.")
        except Exception as e:
            print(f"Se produjo un error al cargar el archivo: {e}")
        
    def mostrarBeneficiarios(self):
        for beneficiario in self.__listaBeneficiarios:
            print(beneficiario)
            
    def ordenar(self):
        self.__listaBeneficiarios = sorted(self.__listaBeneficiarios, reverse=True)
    
    def buscarbeneficiario(self, gestorbeca, becax):
        i=0
        band=False
        cont=0
        id=gestorbeca.getId(becax)
        if id is not None:
            while i< len(self.__listaBeneficiarios):
                if self.__listaBeneficiarios[i].getIdBeca() == id.getIdBeca():
                    print(f"Beneficiario: {self.__listaBeneficiarios[i].getNombre()} {self.__listaBeneficiarios[i].getApellido()}")
                    cont += 1
                    band = True
                i += 1
            if band:
                print(f"La secretaria debe disponer de {id.getImporte() * cont} para el pago de la beca {id.getTipoBeca()}.")
    
    def buscarbeneficiariopordni(self,dni):
        i=0
        band=False
        cont=0
        while i<len(self.__listaBeneficiarios):
            if self.__listaBeneficiarios[i].getDni() == dni:
                cont += 1
                beneficiario= self.__listaBeneficiarios[i]
                band = True
            i += 1
        if band:
            if cont > 1:
                print(f"El beneficiario con DNI {dni} tiene más de una beca. Nombre: {beneficiario.getNombre()}, Apellido: {beneficiario.getApellido()}")
            else:
                print(f"El beneficiario con DNI {dni} no tiene más de una beca.")
        else:
            print(f"No se encontró un beneficiario con el DNI {dni}.")
    
    def promedio(self):
        i=0
        band=False
        while i < len(self.__listaBeneficiarios):
            if self.__listaBeneficiarios[i].getPromedio() > 8 and self.__listaBeneficiarios[i].getIdBeca() != 4:
                print(f"Nombre: {self.__listaBeneficiarios[i].getNombre()}, Apellido: {self.__listaBeneficiarios[i].getApellido()}, Promedio: {self.__listaBeneficiarios[i].getPromedio()} no posee beca de ayuda económica.")
                band = True
            i += 1
        if not band:
            print("No hay beneficiarios con promedio mayor a 8 y sin beca de ayuda económica.")
            

            
            
            
            
            
# if __name__ == "__main__":     
#     manejador = ManejadorBeneficiarios()
#     manejador.cargarcsv()
#     manejador.mostrarBeneficiarios()
#     manejador.ordenar()
#     print("\nLista de beneficiarios ordenada por facultad:")
#     manejador.mostrarBeneficiarios()
        
