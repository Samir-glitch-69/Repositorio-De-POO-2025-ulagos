class Vehiculo:
    def __init__(self, marca, modelo, año, disponible):
        # atributos
        self.__disponible = bool(disponible)
        self.__marca = str(marca)
        self.__modelo = str(modelo)
        self.__año = int(año)
    
    # los getter se pueden usar dentro de las funciones de abajo sin herencia o polimorfismo ( no tenia ni idea )
    # getter para disponible (necesario para acceder desde Concesionaria)
    def esta_disponible(self):
        return self.__disponible
    
    # getter para obtener info del vehículo
    def get_info(self):
        return f"{self.__marca} {self.__modelo} ({self.__año})"
    
    # método marcar vendido que es cuando se compra el vehículo  
    def marcar_vendido(self):
        if self.__disponible:
            print(f"El vehículo {self.get_info()} se ha vendido, pasa a estar no disponible")
            self.__disponible = False
        else:
            print(f"El vehículo {self.get_info()} ya está vendido")
    
    def __str__(self):
        return f"\nDetalles del vehículo: \n\nMarca:  |{self.__marca}|\nModelo: |{self.__modelo}|\nAño:    |{self.__año}|\n\nDisponible?: |{self.__disponible}|\n"

class Concesionaria:
    # para las listas tengo que definir que la lista esta vacia y luego agregar abajo que si no hay nada hay una lista vacia
    def __init__(self, nombre, lista_de_vehiculos=None):
        self.nombre = str(nombre)
        # Si no se pasa una lista, inicializar con lista vacía
        self.lista_de_vehiculos = lista_de_vehiculos if lista_de_vehiculos else []
    
    def agregar_vehiculo(self, vehiculo):
        print(f"Agregando el vehículo al concesionario {self.nombre}")
        self.lista_de_vehiculos.append(vehiculo)
    
    def mostrar_vehiculos(self):
        if not self.lista_de_vehiculos:
            print("No hay vehículos en el concesionario")
            return
        
        print(f"\nVehículos en {self.nombre}:")
        for i, vehiculo in enumerate(self.lista_de_vehiculos, 1):
            print(f"  {i}. {vehiculo.get_info()} - {'Disponible' if vehiculo.esta_disponible() else 'Vendido'}")
    
    def vender_vehiculo(self, indice):
        if 0 <= indice < len(self.lista_de_vehiculos):
            vehiculo = self.lista_de_vehiculos[indice]
            if vehiculo.esta_disponible():
                vehiculo.marcar_vendido()
                print(f"Vehículo vendido exitosamente")
            else:
                print(f"El vehículo ya está vendido")
        else:
            print("Índice de vehículo inválido")

# Ejemplo de uso
vehiculo1 = Vehiculo("Toyota", "Corolla", 2022, True)
vehiculo2 = Vehiculo("Lamborghini", "Urus", 2022, True)

# Crear concesionaria con un vehículo inicial
concesionaria1 = Concesionaria("Diavollo", [vehiculo1])

print("=== Estado inicial ===")
print(vehiculo1)

print("=== Marcando vehículo1 como vendido ===")
vehiculo1.marcar_vendido()
print(vehiculo1)

print("=== Agregando vehículo2 al concesionario ===")
concesionaria1.agregar_vehiculo(vehiculo2)

print("=== Mostrando todos los vehículos ===")
concesionaria1.mostrar_vehiculos()

print("=== Vendiendo vehículo en índice 1 (vehiculo2) ===")
concesionaria1.vender_vehiculo(1)

print("=== Estado final de vehículos ===")
concesionaria1.mostrar_vehiculos()