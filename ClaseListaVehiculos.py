from zope.interface import implementer
from ClaseVehiculo import Vehiculo
from ClaseVehiculoNuevo import VehiculoNuevo
from ClaseVehiculoUsado import VehiculoUsado
from ClaseNodo import Nodo
from InterfazControlador import IControlador
@implementer(IControlador)
class ListaVehiculos:
    __comienzo= None
    __actual= None
    __indice= 0
    __tope= 0
    def __init__(self):
        self.__comienzo= None
        self.__actual= None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice= 0
            raise StopIteration
        else:
            self.__indice += 1
            dato= self.__actual.getVehiculo()
            self.__actual= self.__actual.getSiguiente()
            return dato
    def insertarElemento(self,posicion1,elemento1):
        try:
            if posicion1 > 0:
                i= 1
                nuevo= Nodo(elemento1)
                anterior= None
                p= self.__comienzo
                if posicion1 == 1:
                    nuevo.setSiguiente(self.__comienzo)
                    self.__comienzo= nuevo
                    self.__tope += 1
                    self.__actual= self.__comienzo
                else:
                    while (p != None)and(i < posicion1):
                        anterior= p
                        p= p.getSiguiente()
                        i += 1
                    if p == None:
                        i= i/0
                    anterior.setSiguiente(nuevo)
                    nuevo.setSiguiente(p)
                    self.__tope += 1
                    print("VEHICULO INSERTADO CON EXITO EN LA COLECCION")
            else:
                print("ERROR, La posicion debe ser de 1 en adelante")
        except ZeroDivisionError:
            print("ERROR, La posicion no es valida")
    def agregarElemento(self,elemento2):
        p= None
        nuevo= Nodo(elemento2)
        anterior= None
        if self.__comienzo == None:
            self.__comienzo= nuevo
            self.__tope += 1
            self.__actual = self.__comienzo
        else:
            p= self.__comienzo
            while p != None:
                anterior=p
                p = p.getSiguiente()
            anterior.setSiguiente(nuevo)
            self.__tope += 1
    def mostrarElemento(self,posicion2):
        try:
            if posicion2 > 0:
                i= 1
                aux= self.__comienzo
                while (aux != None)and(i < posicion2):
                    aux = aux.getSiguiente()
                    i += 1
                print("El tipo de objeto almacenado en la posicion {} de la coleccion es: {}".format(posicion2,aux.getVehiculo().__class__.__name__))
            else:
                print("ERROR, La posicion debe ser de 1 en adelante")
        except AttributeError:
            print("ERROR, La posicion no es valida")
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            vehiculos=[Vehiculo.toJSON() for Vehiculo in self]
            )
        return d
    def crearVehiculo(self):
        tipo= int(input("Ingrese el tipo de vehiculo que desea agregar a la coleccion: 1- Vehiculo Usado, 2- Vehiculo Nuevo: "))
        if tipo == 1:
            mod= input('Ingrese el modelo del vehiculo: ')
            cant= int(input('Ingrese la cantidad de puertas: '))
            col= input('Ingrese el color del vehiculo: ')
            pre= int(input('Ingrese el precio base del vehiculo: '))
            mar= input("Ingrese la marca: ")
            pat= input('Ingrese la patente: ')
            Y= int(input('Ingrese el año del vehiculo: '))
            kilo= int(input('Ingrese el kilometraje: '))
            unVehiculoUsado= VehiculoUsado(mod,cant,col,pre,mar,pat,Y,kilo)
            return unVehiculoUsado
        elif tipo == 2:
            print("TODOS LOS VEHICULOS NUEVOS SON DE LA MARCA: {}".format(VehiculoNuevo.getMarca1()))
            mod= input('Ingrese el modelo del vehiculo: ')
            cant= int(input('Ingrese la cantidad de puertas: '))
            col= input('Ingrese el color del vehiculo: ')
            pre= int(input('Ingrese el precio base del vehiculo: '))
            ver= input("Ingrese la version, puede ser base o full: ")
            while (ver.lower() != 'base')and(ver.lower() != 'full'):
                ver= input("Version de vehiculo incorrecta, ingrese nuevamente, puede ser base o full: ")
            unVehiculoNuevo= VehiculoNuevo(mod,cant,col,pre,ver)
            return unVehiculoNuevo
        else:
            print("ERROR, tipo de vehiculo ingresado incorrecto")
            return 1
    def buscarPatente(self,pat):
        bandera= False
        aux= self.__comienzo
        while (aux != None)and(bandera == False):
            if isinstance(aux.getVehiculo(),VehiculoUsado)and(pat == aux.getVehiculo().getPatente()):
                nuevoPrecio= int(input('Ingrese el nuevo precio base del vehiculo con patente {}: '.format(pat)))
                aux.getVehiculo().setPrecioBase(nuevoPrecio)
                print("Precio de venta: {}".format(aux.getVehiculo().importeVenta()))
                bandera= True
            aux= aux.getSiguiente()
        return bandera
    def modPatente(self):
        pat= input("Ingrese patente: ")
        if self.buscarPatente(pat) == False:
            print("ERROR, La patente que ingreso no se encontro en la lista")
    def masEconomico(self):
        minNumero= 999999999
        minVehiculo= None
        aux= self.__comienzo
        while aux != None:
            if minNumero > aux.getVehiculo().getPrecioBase():
                minNumero = aux.getVehiculo().getPrecioBase()
                minVehiculo= aux
            aux= aux.getSiguiente()
        print("VEHICULO MAS ECONOMICO\n{}\nIMPORTE DE VENTA: {}".format(minVehiculo.getVehiculo(),minVehiculo.getVehiculo().importeVenta()))
    def MostrarTodo(self):
        for dato in self:
            print("Modelo: {}, Cantidad de puertas: {}, Importe de venta: {}".format(dato.getModelo(),dato.getCantidadPuertas(),dato.importeVenta()))
