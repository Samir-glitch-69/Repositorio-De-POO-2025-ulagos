# Creando el constructor
class Gato():
    # Atributos de los gatos o felinos
    def __init__(self, nombre, edad, lvl_energia, lvl_hambre):
        self.nombre = str(nombre)
        self.__edad = int(edad)
        self.__lvl_energia = int(lvl_energia)
        self.__lvl_hambre = int(lvl_hambre)
        self.__cantidades_de_cambio_de_nombre = 0
    
    # Realizando los get ( getter )

    def get_edad(self):
        return self.__edad
        
    def get_lvl_energia(self):
        return self.__lvl_energia

    def get_lvl_hambre(self):
        return self.__lvl_hambre
    
    def get_cantidad_cambio_de_nombre(self):
        return self.__cantidades_de_cambio_de_nombre

    # Función de gatos jugando - pierden 5 de hambre y energía
    def cats_playing(self):
        # Restamos 5 a energía y hambre (pero no menos de 0)
        self.__lvl_energia = max(0, self.__lvl_energia - 5)
        self.__lvl_hambre = max(0, self.__lvl_hambre - 5)
        
        print(f"El gato |{self.nombre}| está jugando!")
        print(f"Energía: {self.__lvl_energia} | Hambre: {self.__lvl_hambre}")

    # Función de los gatos comiendo - recuperan energía y sacian hambre
    def cat_eating(self):
        # Sumamos 5 a energía y hambre (pero no más de 100)
        self.__lvl_energia = min(100, self.__lvl_energia + 5)
        self.__lvl_hambre = min(100, self.__lvl_hambre + 5)
        
        print(f"El gato {self.nombre} está comiendo!")
        print(f"Energía: {self.__lvl_energia} | Hambre: {self.__lvl_hambre}")

    # Función de info de los gatos
    def __str__(self):
        return (f"Gato: {self.nombre}, Edad: {self.__edad} años, "
                f"Energía: {self.__lvl_energia}, Hambre: {self.__lvl_hambre}")

    # Función del destructor
    def __del__(self):
        print(f"El gato {self.nombre} se escapó de la cafetería malvada :( ")


# Creando la clase del espacio del café
class Espacio_Cafe():
    def __init__(self, nombre_espacio, capacidad_maxima):
        self.nombre_espacio = str(nombre_espacio)
        self.capacidad_maxima = int(capacidad_maxima)
        self.__gatos_en_espacio = []  # Lista de objetos Gato

    # Método para mover un gato al espacio
    def mover_gato(self, gato):
        # Verificamos si hay espacio
        if len(self.__gatos_en_espacio) >= self.capacidad_maxima:
            print(f"¡Excede la cantidad máxima de gatos en |{self.nombre_espacio}|!")
            return False
        else:
            # Añadimos el gato a la lista
            self.__gatos_en_espacio.append(gato)
            print(f"El gato {gato.nombre} se movió hacia |{self.nombre_espacio}|")
            return True

    # Método para remover un gato del espacio
    def remover_gato(self, gato):
        if gato in self.__gatos_en_espacio:
            self.__gatos_en_espacio.remove(gato)
            print(f"El gato {gato.nombre} salió de |{self.nombre_espacio}|")
            return True
        else:
            print(f"El gato {gato.nombre} no está en |{self.nombre_espacio}|")
            return False

    # Mostrar información de los gatos en el espacio
    def info_gatos(self):
        if not self.__gatos_en_espacio:
            print(f"No hay gatos en |{self.nombre_espacio}|")
        else:
            print(f"\nGatos en |{self.nombre_espacio}|:")
            for gato in self.__gatos_en_espacio:
                print(f"  - {gato}")

    # Información del espacio
    def info_espacio(self):
        ocupacion = len(self.__gatos_en_espacio)
        print(f"\nEspacio: {self.nombre_espacio}")
        print(f"Capacidad: {ocupacion}/{self.capacidad_maxima}")


# Definiendo a los gatos (CORRECCIÓN: crear objetos, no tuplas) 
# Me ayude con ia no sabia en que me habia equivocado este fue el error principal
gato1 = Gato("Piskolita", 3, 95, 100)
gato2 = Gato("Roun", 8, 80, 100)
gato3 = Gato("Cervei", 4, 90, 100)
gato4 = Gato("Dimitri", 7, 85, 100)
gato5 = Gato("Vodki", 5, 100, 100)
gato6 = Gato("Kurvi", 1, 100, 100)

# Definiendo espacios del café
espacio1 = Espacio_Cafe("Cocina", 3)
espacio2 = Espacio_Cafe("Hall Central", 5)

# Ejemplo de uso
print("=== CAFETERÍA DE GATOS ===\n")

# Mostrando información inicial de los gatos
print("Gatos disponibles:")
for i, gato in enumerate([gato1, gato2, gato3, gato4, gato5, gato6], 1):
    print(f"{i}. {gato}")

print("\n" + "="*40)

# Moviendo gatos a diferentes espacios
espacio1.mover_gato(gato1)
espacio1.mover_gato(gato2)
espacio2.mover_gato(gato3)
espacio2.mover_gato(gato4)

# Mostrando información de los espacios
espacio1.info_espacio()
espacio1.info_gatos()

espacio2.info_espacio()
espacio2.info_gatos()

# Haciendo que los gatos jueguen y coman
print(f"\n{'-'*40}")
print("¡Los gatos están activos!")
gato1.cats_playing()
gato1.cat_eating()

print(f"\n¿Qué pasa si intentamos meter demasiados gatos?")
espacio1.mover_gato(gato5)  # Ya hay 2 gatos, capacidad es 3
espacio1.mover_gato(gato6)  # Ya hay 3 gatos, este debería fallar

espacio1.info_espacio()
espacio1.info_gatos()

# Los gatos se borran ( del ) automaticamente cuando no son referenciados mas por memoria