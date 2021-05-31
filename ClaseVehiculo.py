class Vehiculo:
    __modelo= ''
    __cantPuertas= 0
    __color= ''
    __precioBase= 0
    def __init__(self,mod='',cant=0,col='',pre=0):
        self.__modelo= mod
        self.__cantPuertas= cant
        self.__color= col
        self.__precioBase= pre
    def toJSON(self):
        pass
    def importeVenta(self):
        pass
    def setPrecioBase(self,nuevoPrecio):
        self.__precioBase= nuevoPrecio
    def getModelo(self):
        return self.__modelo
    def getCantidadPuertas(self):
        return self.__cantPuertas
    def getColor(self):
        return self.__color
    def getPrecioBase(self):
        return self.__precioBase
