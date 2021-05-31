from ClaseVehiculo import Vehiculo
from ClaseObjectEncoder import ObjectEncoder
from ClaseListaVehiculos import ListaVehiculos
if __name__=='__main__':
    jsonF=ObjectEncoder()
    d= jsonF.leerJSONArchivo('vehiculos.json')
    Vehiculos= jsonF.decodificarDiccionario(d)
    while True:
        print("_____MENU DE OPCIONES_____")
        print("[1]...Insertar un vehículo en la colección en una posición determinada")
        print("[2]...Agregar un vehiculo a la coleccion")
        print("[3]...Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición")
        print("[4]...Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta")
        print("[5]...Mostrar todos los datos, incluido el importe de venta, del vehículo más económico")
        print("[6]...Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta")
        print("[7]...Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”")
        print("[0]...Salir")
        try:
            op= int(input('Seleccione una opcion: '))
            if op in range(8):
                if op == 1:
                    nuevoVehiculo= Vehiculos.crearVehiculo()
                    if isinstance(nuevoVehiculo,Vehiculo):
                        posicion1= int(input('Ingrese la posicion de la lista en la que desea insertar el vehiculo: '))
                        Vehiculos.insertarElemento(posicion1,nuevoVehiculo)
                if op == 2:
                    nuevoVehiculo1= Vehiculos.crearVehiculo()
                    if isinstance(nuevoVehiculo1,Vehiculo):
                        Vehiculos.agregarElemento(nuevoVehiculo1)
                if op == 3:
                    posicion2= int(input('Ingrese la posicion de la lista: '))
                    Vehiculos.mostrarElemento(posicion2)
                if op == 4:
                    Vehiculos.modPatente()
                if op == 5:
                    Vehiculos.masEconomico()
                if op == 6:
                    Vehiculos.MostrarTodo()
                if op == 7:
                    d= Vehiculos.toJSON()
                    jsonF.guardarJSONArchivo(d,'vehiculos.json')
                if op == 0:
                    print("_____MENU FINALIZADO_____")
                    break
            else:
                print("ERROR, solo puede ingresar numeros del 0 al 7")
        except ValueError:
            print("ERROR, ingrese solamente numeros")
