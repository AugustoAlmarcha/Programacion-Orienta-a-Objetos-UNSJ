import csv


import numpy as np


from claseconexiones import *

class Gestorconexiones:
    __cantidad:int
    __dimension:int
    __incremento:int
    __arregloconexiones:np.ndarray
    
    def __init__(self):
        self.__cantidad=0
        self.__dimension=10
        self.__incremento=5
        self.__arregloconexiones=np.empty(self.__dimension,dtype=Conexiones)
        
    def agregarConexion(self,conexion:Conexiones):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arregloconexiones.resize(self.__dimension)
        self.__arregloconexiones[self.__cantidad]=conexion
        self.__cantidad+=1
    
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\Extraordinario\conexiones.csv") 
            reader=csv.reader(archivo,delimiter=";")
            next(reader)
            for fila in reader:
                self.agregarConexion(Conexiones(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]),int(fila[5])))
            archivo.close()
        except Exception as e:
            print(f'Error al cargar el archivo: {e}')
        except FileNotFoundError:
            print('No se encontro el archivo')
            
    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__arregloconexiones[i])
            
    def mostrarConexiones(self,dni,gamerx):
        i=0
        contador=0
        gamer=gamerx.BuscarGamer(dni)
        if gamer is None:
            print('No se encontro el gamer')
        else:
            print(f"DNI: {gamer.getDni()} , Nombre: {gamer.getNombre()} , Apellido: {gamer.getApellidos()}")
            print(f"Alias: {gamer.getAlias()} , Plan: {gamer.getPlan()}, Importe Base: {gamer.getImporteBase()}")
            while i<self.__cantidad:
                if gamer.getIdJugador()==self.__arregloconexiones[i].getIdJugador():
                    print(self.__arregloconexiones[i])
                    contador+=(self.__arregloconexiones[i].getHoraDeFin()-self.__arregloconexiones[i].getHoraDeInicio())
                i+=1
            horasexcedidas=contador-gamer.getTiempoLimite()
            print(f"Total de horas jugadas: {contador}")
            horaextra = 0
            if horasexcedidas>0:
                print(f"Horas excedidas: {horasexcedidas}")
                if gamer.getPlan() == "Basico":
                    horaextra = horasexcedidas * (gamer.getImporteBase() * 0.25)
                elif gamer.getPlan() == "Completo":
                    horaextra = horasexcedidas * (gamer.getImporteBase() * 0.30)
                elif gamer.getPlan() == "Extendido":
                    horaextra = horasexcedidas * (gamer.getImporteBase() * 0.40)
            else:
                print("No excedio el tiempo limite")
                horaextra=0
            print(f"Importe Total: {gamer.getImporteBase() + horaextra}")
            
    def BuscarJuego(self,juego,gamerx):
        i=0
        band=False
        while i < self.__cantidad:
            if juego == self.__arregloconexiones[i].getNombreDelJuego():
                print("Se encontro el Juego")
                band=True    
                gamer=gamerx.BuscarGamerporId(self.__arregloconexiones[i].getIdJugador())
                print(f"{self.__arregloconexiones[i].getDireccionIp()}, {gamer.getNombre()}, {gamer.getApellidos()}, {gamer.getAlias()}, {gamer.getPlan()}")    
            i+=1
        if band is False:
            print("No se encontro el juego que busca")
    
    def ordenar(self):
        self.__arregloconexiones=sorted(self.__arregloconexiones)
        
    def Listadomismo(self,gamerx):
        i=1
        band=False
        while i<self.__cantidad:
            if bool(self.__arregloconexiones[i] == self.__arregloconexiones[i-1]):
                datos=gamerx.BuscarGamerporId(self.__arregloconexiones[i].getIdJugador())
                if datos.getPlan() == "Basico":
                    band=True
                    print(f"El usuario {datos.getNombre()} {datos.getApellido()} con ID : {datos.getIdJugador()} se conecta en horas simultaneas con plan basico")
            i+=1
        if band is False:
            print("No se encontraron usuarios con conexiones multiples")
                

        
            
        
                    
 
                
            
            
            
    
    
# if __name__=="__main__":
#     gestor=Gestorconexiones()
#     gestor.cargarcsv()
#     gestor.mostrar()
    