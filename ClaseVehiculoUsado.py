import json
from pathlib import Path
from ClaseVehiculo import Vehiculo
from datetime import date
class VehiculoUsado(Vehiculo):
    __marca2= ''
    __patente= ''
    __Year= 0
    __kilometraje= 0
    def __init__(self,mod='',cant=0,col='',pre=0,mar='',pat='',Y=0,kilo=0):
        super().__init__(mod,cant,col,pre)
        self.__marca2= mar
        self.__patente= pat
        self.__Year= Y
        self.__kilometraje= kilo
    def __str__(self):
        print("VEHICULO USADO")
        return 'Modelo: {}, Cantidad Puertas: {}, Color: {}, Precio Base: {}, Marca: {}, Patente: {}, Año: {}, Kilometraje: {}'.format(super().getModelo(),super().getCantidadPuertas(),super().getColor(),super().getPrecioBase(),self.__marca2,self.__patente,self.__Year,self.__kilometraje)
    def getPatente(self):
        return self.__patente
    def importeVenta(self):
        Base2= self.getPrecioBase()
        Hoy= date.today()
        Total2= Base2 - ((Base2 * 0.01)*(Hoy.year - self.__Year))
        if self.__kilometraje > 100000:
            Total2 -= Base2 * 0.02
        return Total2
    def toJSON(self):
        d= dict(
            __class__= self.__class__.__name__,
            __atributos__=dict(
                mod=super().getModelo(),
                cant=super().getCantidadPuertas(),
                col=super().getColor(),
                pre=super().getPrecioBase(),
                mar=self.__marca2,
                pat=self.__patente,
                Y=self.__Year,
                kilo=self.__kilometraje
                     )
            )
        return d
