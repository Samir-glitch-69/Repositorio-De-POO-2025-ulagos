# Ejemplo de clase en Python
class Animal():
    # Constructor de la clase Animal
    # Atributos de la clase animal (características compartidas por todos los objetos de la clase)
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    # Métodos de la clase animal (comportamientos)
    def correr(self):
        print(f"{self.nombre} está corriendo")

    def dormir(self):
        print(f"{self.nombre} está durmiendo")

# Creando un objeto de la clase Animal
gatito = Animal("Michi", "Gato", 4) 
perrito = Animal("Firulais", "Perro", 2)
loro = Animal("Loro Pepito", "Ave", 1)

# Impresión de los atributos de los objetos
print(f"El nombre del animal es: {gatito.nombre}")
print(f"La especie del animal es: {perrito.nombre}")
print(f"La especie del animal es: {loro.nombre}")

# Llamada a los métodos de los objetos
gatito.correr()
perrito.correr()
loro.dormir()