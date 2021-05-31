from ClaseVehiculoNuevo import VehiculoNuevo
from ClaseVehiculoUsado import VehiculoUsado
from ClaseListaVehiculos import ListaVehiculos
import json
from pathlib import Path
class ObjectEncoder:
    def decodificarDiccionario(self,d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='ListaVehiculos':
                vehiculos=d['vehiculos']
                listaV=class_()
                for i in range(len(vehiculos)):
                    dVehiculo=vehiculos[i]
                    class_name=dVehiculo.pop('__class__')
                    class_=eval(class_name)
                    atributos=dVehiculo['__atributos__']
                    unVehiculo=class_(**atributos)
                    listaV.agregarElemento(unVehiculo)
            return listaV
    def guardarJSONArchivo(self,diccionario,archivo):
        with Path(archivo).open("w",encoding="UTF-8") as destino:
            json.dump(diccionario,destino,indent=4)
            destino.close()
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario= json.load(fuente)
            fuente.close()
            return diccionario
