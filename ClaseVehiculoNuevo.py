from ClaseVehiculo import Vehiculo
class VehiculoNuevo(Vehiculo):
    Marca1= 'Tesla'
    __version= ''
    def __init__(self,mod='',cant=0,col='',pre=0,ver=''):
        super().__init__(mod,cant,col,pre)
        self.__version= ver
    def __str__(self):
        print("VEHICULO NUEVO")
        return 'Modelo: {}, CantPuertas: {}, Color: {}, PrecioBase: {}, Marca: {}, Version: {}'.format(super().getModelo(),super().getCantidadPuertas(),super().getColor(),super().getPrecioBase(),self.Marca1,self.__version)
    @classmethod
    def getMarca1(cls):
        return cls.Marca1
    def importeVenta(self):
        Base1= self.getPrecioBase()
        Total1= Base1 + (Base1 * 0.1)
        if self.__version == 'full':
            Total1 += Base1 * 0.02
        return Total1
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                mod=super().getModelo(),
                cant=super().getCantidadPuertas(),
                col=super().getColor(),
                pre=super().getPrecioBase(),
                ver=self.__version
                      )
            )
        return d
