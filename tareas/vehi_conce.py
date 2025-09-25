class Vehiculo:
    def __init__(self, marca, modelo, año, disponible):
        # atributos
        self.__disponible = bool(disponible)
        self.__marca = str(marca)
        self.__modelo = str(modelo)
        self.__año = int(año)

    # metodo marcar vendido que es cuando se compra el vehiculo 

    def marcar_vendido(self):
        print(f"El vehiculo se ha vendido pasa a estar no disponible")
        self.__disponible = False

    def __str__(self):
        return F"\nDetalles del vehiculo: \n\nMarca:  |{self.__marca}|\nModelo: |{self.__modelo}|\nAño:    |{self.__año}|\n\nDisponible?: |{self.__disponible}|\n"

class Concesionaria:
    def __init__(self, nombre, lista_de_vehiculos):
        self.nombre = str(nombre)
        self.lista_de_vehiculos = []

    def agregar_vehiculo(self, ):
        print(f"Agregando el vehiculo al concesionario")
        self.lista_de_vehiculos.append(Vehiculo)

    def mostrar_vehiculos(self):

            for Vehiculo in self.lista_de_vehiculos:
                print(f"  - {Vehiculo}")

    def vender_vehiculo(self):
        if self.Vehiculo == False:
            print(f"El vehiculo fue vendido")
        elif Vehiculo == True:
            print(f"El vehiculo esta disponible procediendo a venderlo")
            Vehiculo == False

vehiculo1 = Vehiculo("Toyota", "Corolla", 2022, True)
vehiculo2 = Vehiculo("lambo", "urus", 2022, True)

concesionaria1 = Concesionaria("Diavollo", [vehiculo1])

print(vehiculo1)
vehiculo1.marcar_vendido()
print(vehiculo1)

concesionaria1.agregar_vehiculo()
concesionaria1.mostrar_vehiculos()
concesionaria1.vender_vehiculo()
concesionaria1.mostrar_vehiculos
