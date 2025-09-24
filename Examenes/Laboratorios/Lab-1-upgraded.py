try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
# el try de los colores de colorama para el codigo fore = texto, back la parte de atras, style la forma del texto
except ImportError:
    print("Para instalar colorama: pip install colorama")
    COLORAMA_AVAILABLE = False
    class FakeColor:
        def __getattr__(self, name): return ""
    Fore = Back = Style = FakeColor()
    # el except es para devolver un espacio vacio "" si es que la persona no tiene el colorama instalado

# Creando el constructor
class Gato():
    
    # Atributos de los gatos
    def __init__(self, nombre, edad, lvl_energia, lvl_hambre):
        # Mejorando con encapsulacion a variables que no deberieran cambiarse
        # Aprendiendo que no todos los atributos tienen que ser parte del objeto comocaant-de-cambio-de-nmombre
        self.nombre = str(nombre)
        self.__edad = int(edad)
        self.__lvl_energia = int(lvl_energia)
        self.__lvl_hambre = int(lvl_hambre)
        self.__cantidades_de_cambio_de_nombre = 0

    # Realizando los set ( setters )
    # Los setters son formas de darle una variable al atributo del objeto mas un comentario de ia d comofuncionan los setters
    """¡SÍ, LOS SETTERS FUNCIONAN PERFECTAMENTE CON ATRIBUTOS PRIVADOS!
Esa es precisamente la razón principal de crear setters: dar acceso controlado a atributos privados.
Cómo funciona:
pythonclass Gato:
    def __init__(self):
        self.__energia = 100  # ← PRIVADO

    def set_lvl_energia(self, new_energy):  # ← SETTER
        if 0 <= new_energy <= 100:
            self.__energia = new_energy  # ✅ Funciona desde DENTRO de la clase
Desde FUERA de la clase:
pythongato1 = Gato()

# ❌ ESTO NO FUNCIONA (atributo privado)
gato1.__energia = 50  # Error: no puede acceder

# ✅ ESTO SÍ FUNCIONA (a través del setter)
gato1.set_lvl_energia(50)  # Funciona perfectamente"""
    def set_nombre(self, new_nombre):
        if not new_nombre or new_nombre.strip() == "":
            print(f"{Fore.RED}El nombre no puede estar vacio")
            return False
        if len(new_nombre) > 15:
            print(f"{Fore.RED}el nombre tiene que ser menor a 15 caracteres")
            return False
        if new_nombre == self.nombre:
            print(f"{Fore.YELLOW}el gato tiene el mismo nombre")
            return False

        print(f"{Fore.GREEN}Cambiando nombre {self.nombre} a {new_nombre}")    
        self.nombre = new_nombre
        self.__cantidades_de_cambio_de_nombre += 1
        print(f"{Fore.GREEN}El gato a cambiado {self.__cantidades_de_cambio_de_nombre}")
        return True
    
    def set_edad(self):
        print(f"{Fore.RED}no se puede modificar la edad de un gato!!")
        print(f"{Fore.BLUE}Edad actual: {self.__edad}")

    def set_lvl_energia(self, new_energy):
        if 0 <= new_energy <= 100:
            self.__lvl_energia = new_energy
            print(F"{Fore.GREEN}energia establecida a {new_energy}")
        else:
            print(F"{Fore.RED}la energia debe estar entre 0 y 100")
    
    def set_lvl_hambre(self, new_hambre):
        if new_hambre < 0:
            print(f"{Fore.YELLOW}hambre muy baja, estableciendo minimo 0")
            self.__lvl_hambre = 0
        elif new_hambre > 100:
            print(f"{Fore.YELLOW}hambre muy alta estableciendo el maximo 100")
            self.__lvl_hambre = 100
        else:
            self.__lvl_hambre = new_hambre
            print(f"{Fore.GREEN}hambre establecida a {new_hambre}")

    # Realizando los get ( getter )
    # Se realizan para poder tener la info de un atributo en el instante
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
        # Restamos 5 a energía y hambre (pero no menos de 0) ( hecho por ia lo tenia malo )
        self.__lvl_energia = max(0, self.__lvl_energia - 5)
        self.__lvl_hambre = max(0, self.__lvl_hambre - 5)
        
        print(f"{Fore.CYAN}El gato |{self.nombre}| está jugando!")
        print(f"{Fore.BLUE}Energía: {self.__lvl_energia} | Hambre: {self.__lvl_hambre}")

    # Función de los gatos comiendo - recuperan energía y sacian hambre
    def cat_eating(self):
        # Sumamos 5 a energía y hambre (pero no más de 100) ( hecho por ia lo tenia malo )
        self.__lvl_energia = min(100, self.__lvl_energia + 5)
        self.__lvl_hambre = min(100, self.__lvl_hambre + 5)
        
        print(f"{Fore.CYAN}El gato {self.nombre} está comiendo!")
        print(f"{Fore.BLUE}Energía: {self.__lvl_energia} | Hambre: {self.__lvl_hambre}")

    # Función de info de los gatos
    def __str__(self):
        # Me falto el return
        return (f"{Fore.BLUE}Gato: {self.nombre}, Edad: {self.__edad} años, "
                f"Energía: {self.__lvl_energia}, Hambre: {self.__lvl_hambre}")

    # Función del destructor
    def __del__(self):
        print(f"{Fore.YELLOW}El gato {self.nombre} se escapó de la cafetería malvada :( ")

# Creando el constructor de los gatorobot
class Gatorobot(Gato):
    # Se coloca entre parentesis la la clase padre d la cual se bajan los atributos
    def __init__(self, nombre, edad, lvl_energia, lvl_hambre):
        super().__init__(nombre, edad, lvl_energia, lvl_hambre)
        # El super realiza lo de abajo con herencia de la clase principal
        #self.__nombre = str(__nombre) no se coloca nombre por la herencia duhu
        """self.nombre = str(nombre)
        self.__edad = int(edad)
        self.__lvl_energia = int(lvl_energia)
        self.__lvl_hambre = int(lvl_hambre)
        self.__cantidades_de_cambio_de_nombre = 0"""

        self.__bateria = 100
        self.__aceite = 100
        self.__version = "1.0"

    # Realizando los set ( setters )
    def set_bateria(self, new_bateria):
        if 0 <= new_bateria <= 100:
            print(f"🔋 {Fore.GREEN}Batería cambiada de {self.__bateria}% a {new_bateria}%")
            self.__bateria = new_bateria
            return True
        else:
            print(f"{Fore.RED}bateria seleccionada incorrecta")
            return False

    def set_aceite(self, new_aceite):
        if 0 <= new_aceite <= 100:
            print(F"{Fore.GREEN}el aceite seleccionado es correcto:{new_aceite}, cambiando {self.__aceite}")
            self.__aceite = new_aceite
            return True
        else:
            print(f"{Fore.RED}aceite seleccionada incorrecta")
            return False
        
    # en str no funciona por la complejidad de diferencias las versiones
    # en float tampoco por decimales como 1.9 y 1.10 1.10 es mayor pero en decimales en menor 
    # me costo una banda par poder hacerlo solo me ayude con ia y quede loco

    def set_version(self, new_version):
        # 1. Manejo del caso de cadena vacía o formato incorrecto.
        if not new_version:
            print(f"{Fore.RED}Error: Versión inválida o vacía.")
            return False

        try:
            # 2. Convertir las versiones a listas de números enteros para una comparación precisa.
            current_parts = [int(p) for p in self.__version.split('.')]
            new_parts = [int(p) for p in new_version.split('.')]
        except ValueError:
            # Capturar errores si alguna parte de la versión no es un número.
            print(f"{Fore.RED}Error: El formato de la versión no es numérico (ej: '1.0').")
            return False

        # 3. Comparar las listas de números.
        if new_parts > current_parts:
            print(f"{Fore.GREEN}La versión {new_version} es correcta, actualizando...")
            self.__version = new_version
            return True
        elif new_parts == current_parts:
            print(f"{Fore.YELLOW}Las versiones no pueden ser las mismas.")
            return False
        else:  # new_parts < current_parts
            print(f"{Fore.RED}La versión no puede ser desactualizada, debe ser la más reciente.")
            return False
        # como funciona? se da la version en strings como 1.0 123.543.123 y que es lo que hace?
        # separa los digitos por coma [1, 0] y [123, 543, 123] y los va comparando para ver cual es el mayo
        # y da un true o false por la comparacion de abajo de new parts o current parts

    # Realizando los get ( getter )

    def get_bateria(self):
        return self.__bateria

    def get_aceite(self):
        return self.__aceite

    def get_version(self):
        return self.__version

    # Funciónes propias de los gato robot

    def cambio_de_baterias(self):
        print(f"{Fore.GREEN}Cambiando las baterias de {self.__bateria} a 100%")
        self.__bateria = 100

    def cambio_de_aceite(self):
        print(f"{Fore.GREEN}Cambiando el aceite de {self.__aceite} a 100%")
        self.__aceite = 100

    def primera_version(self):
        print(f"{Fore.BLUE}cambiando la version {self.__version} a la primera")
        self.__version = "1.0"

    # creando el polimorfismo de las anteriores funciones del gato principal ( clase principal ), 
    # el primer ejemplo con ia por que no entendia como funcionaba

    # se coloca la misma funcion de la herencia o del gato principal y se modifica la clase a otra para que 
    # cambie su funcion cuando se usa en un gato robot
    def cats_playing(self):
        # Los robots juegan diferente - gastan batería en lugar de solo energía
        if self.__bateria < 10:
            print(f"🔋 {Fore.RED}Batería muy baja para jugar")
            return False

        # Tu lógica especial aquí
        self.__bateria = max(0, self.__bateria - 3)  # Gastar batería
        # También gastar energía normal (llamar al método original)
        # super().cats_playing()  # ← Ejecuta el método del padre también esto es para hacer doble funciones una dentro de otra
        # pero un gato no es igual a un gatorobot

        print(f"🤖 {Fore.MAGENTA}MODO JUEGO ROBOT ACTIVADO")
        print(f"{Fore.BLUE}Batería restante: {self.__bateria}%")
        return True
    
    def cat_eating(self):
        print(F"{Fore.RED}Los gatos roboticos no pueden comer, le diste un corto circuito y perdio 5 de aceite")
        self.__aceite = max(0, self.__aceite - 5)

# Creando la clase del espacio del café
class Espacio_Cafe():
    def __init__(self, nombre_espacio, capacidad_maxima):
        self.nombre_espacio = str(nombre_espacio)
        self.__capacidad_maxima = int(capacidad_maxima)
        self.__gatos_en_espacio = []  # Lista de objetos Gato

    # Método para mover un gato al espacio
    def mover_gato(self, gato):
        # Verificamos si hay espacio
        # Lo tenia malo, era con el propio gatos y la capacidad maxima
        if len(self.__gatos_en_espacio) >= self.__capacidad_maxima:
            print(f"{Fore.RED}¡Excede la cantidad máxima de gatos en |{self.nombre_espacio}|!")
            return False
        else:
            # Añadimos el gato a la lista
            # Algo cerca pero con errores de sintaxis
            self.__gatos_en_espacio.append(gato)
            print(f"{Fore.GREEN}El gato {gato.nombre} se movió hacia |{self.nombre_espacio}|")
            return True

    # Método para remover un gato del espacio
    def remover_gato(self, gato):
        # Algo cerca pero con errores de sintaxis
        if gato in self.__gatos_en_espacio:
            self.__gatos_en_espacio.remove(gato)
            print(f"{Fore.YELLOW}El gato {gato.nombre} salió de |{self.nombre_espacio}|")
            return True
        else:
            print(f"{Fore.RED}El gato {gato.nombre} no está en |{self.nombre_espacio}|")
            return False

    # Mostrar información de los gatos en el espacio
    # Algo cerca pero con errores de sintaxis
    def info_gatos(self):
        if not self.__gatos_en_espacio:
            print(f"{Fore.YELLOW}No hay gatos en |{self.nombre_espacio}|")
        else:
            print(f"\n{Fore.CYAN}Gatos en |{self.nombre_espacio}|:")
            for gato in self.__gatos_en_espacio:
                print(f"  - {gato}")

    # Información del espacio
    def info_espacio(self):
        ocupacion = len(self.__gatos_en_espacio)
        print(f"\n{Fore.CYAN}Espacio: {self.nombre_espacio}")
        print(f"{Fore.BLUE}Capacidad: {ocupacion}/{self.__capacidad_maxima}")


# Definiendo a los gatos (CORRECCIÓN: crear objetos, no tuplas) 
# Me ayude con ia no sabia en que me habia equivocado este fue el error principal
gato1 = Gato("Piskolita", 3, 95, 100)
gato2 = Gato("Roun", 8, 80, 100)
gato3 = Gato("Cervei", 4, 90, 100)
gato4 = Gato("Dimitri", 7, 85, 100)
gato5 = Gato("Vodki", 5, 100, 100)
gato6 = Gato("Kurvi", 1, 100, 100)

# Creando gato robot para probar
robot1 = Gatorobot("R2D2", 2, 85, 90)

# Definiendo espacios del café
espacio1 = Espacio_Cafe("Cocina", 3)
espacio2 = Espacio_Cafe("Hall Central", 5)

# Ejemplo de uso
print(f"\n{Fore.CYAN + Style.BRIGHT}=== CAFETERÍA DE GATOS ===\n")

# Mostrando información inicial de los gatos
print(f"{Fore.MAGENTA}Gatos disponibles:")
for i, gato in enumerate([gato1, gato2, gato3, gato4, gato5, gato6], 1):
    print(f"{i}. {gato}")

print(f"\n{Fore.MAGENTA}Gatos Robot disponibles:")
print(f"1. {robot1}")

print("\n" + "="*40)

# Moviendo gatos a diferentes espacios
espacio1.mover_gato(gato1)
espacio1.mover_gato(gato2)
espacio2.mover_gato(gato3)
espacio2.mover_gato(gato4)
espacio2.mover_gato(robot1)

# Mostrando información de los espacios
espacio1.info_espacio()
espacio1.info_gatos()

espacio2.info_espacio()
espacio2.info_gatos()

# Haciendo que los gatos jueguen y coman
print(f"\n{'-'*40}")
print(f"{Fore.CYAN + Style.BRIGHT}¡Los gatos están activos!")
gato1.cats_playing()
gato1.cat_eating()

print(f"\n{Fore.MAGENTA + Style.BRIGHT}Probando el gato robot:")
robot1.cats_playing()
robot1.cat_eating()

print(f"\n{Fore.CYAN}Probando funciones del robot:")
print(f"Batería actual: {robot1.get_bateria()}%")
print(f"Aceite actual: {robot1.get_aceite()}%")
robot1.cambio_de_baterias()
robot1.cambio_de_aceite()

print(f"\n{Fore.CYAN}Probando setters del robot:")
robot1.set_bateria(75)
robot1.set_version("2.1")

print(f"\n¿Qué pasa si intentamos meter demasiados gatos?")
espacio1.mover_gato(gato5)  # Ya hay 2 gatos, capacidad es 3
espacio1.mover_gato(gato6)  # Ya hay 3 gatos, este debería fallar

espacio1.info_espacio()
espacio1.info_gatos()

# Los gatos se borran ( del ) automaticamente cuando no son referenciados mas por memoria