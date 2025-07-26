from clasepedido import *
import csv

class Gestorpedidos:
    __lista:list
    
    def __init__(self):
        self.__lista=[]
        
    def agregar(self,algo):
        self.__lista.append(algo)
        
    def cargar(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\Ejercicio 4\datospedidos.csv")
            reader= csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                self.agregar(Pedido((fila[0]), int(fila[1]), (fila[2]), float(fila[3]), float(fila[4]), float(fila[5])))
            archivo.close()
        except FileNotFoundError:
            print("El archivo CSV no se encontró.")
        except Exception as e:
            print("Error al leer el archivo CSV:", e)
            
    def mostrar(self):
        for i in self.__lista:
            print(i)
            
    def ordenar(self):
        self.__lista=sorted(self.__lista)
        
    def modificar(self):
        patente=input("Ingrese numero de patente del pedido que quiere modificar")
        id=int(input("Ingrese el id del pedido que busca"))
        tiemporealdeentrega=float(input("Ingrese el tiempo real de entrega"))
        band=False
        i=0
        while i<len(self.__lista) and band is False:
            if self.__lista[i].getpatente() == patente and self.__lista[i].getidpedido()==id:
                self.__lista[i].settiemporeal(tiemporealdeentrega)
                print("Se modifico el tiempo real")
                band=True
            i+=1
        if band is False:
            print("No se encontro pedido con esa patente y id")
    
    def tiempopromedio(self,patente):
        total=0
        aux=0
        for item in self.__lista:
            if item.getpatente() == patente:
                total+=item.gettiemporeal()
                aux+=1
        print(f"El tiempo promedio real de entrega es de {total/aux}")
        
    def listado(self,motox):
        for moto in motox:
            print("--------------")
            print(f"{moto.getpatente()}")
            print(f"{moto.getnya()}")
            total=0
            band=False
            for item in self.__lista:
                if item.getpatente() == moto.getpatente():
                    print(f"{item.getidpedido()}, {item.gettiempoestimado()}, {item.gettiemporeal()}, {item.getprecio()}")
                    total+=item.getprecio()
                    band=True
            if band:
                print(f"El total de la moto {moto.getpatente()} es de {total}")
                print(f"La comision que se queda es de {total*0.2}")
            else:
                print(f"La moto {moto.getpatente()} no tiene pedidos")
    
    def lista(self,motox):
        i=0
        datos=motox.buscarymostrar(i)
        while datos: 
            print(f"{datos.getpatente()}")
            print(f"{datos.getnya()}")
            total=0
            band=False
            for item in self.__lista:
                if item.getpatente() == datos.getpatente():
                    print(f"{item.getidpedido()}, {item.gettiempoestimado()}, {item.gettiemporeal()}, {item.getprecio()}")
                    total+=item.getprecio()
                    band=True
            if band:
                print(f"El total de la moto {datos.getpatente()} es de {total}")
                print(f"La comision que se queda es de {total*0.2}")
            else:
                print(f"La moto {datos.getpatente()} no tiene pedidos")
            i+=1
            datos=motox.buscarymostrar(i)
                
                    
            
        
                
                    
                
            
        
            
                
            

        
        
# if __name__ == "__main__":
#     pedidos=Gestorpedidos()
#     pedidos.cargar()
#     pedidos.mostrar()
#     pedidos.ordenar()
#     print("---------------")
#     pedidos.mostrar()
            