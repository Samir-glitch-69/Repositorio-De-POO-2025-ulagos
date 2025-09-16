"""
🐱 SIMULADOR DE CAFETERÍA DE GATOS 🐱
Versión mejorada con colores, efectos y funcionalidades avanzadas
"""

import random
import time
from enum import Enum

# Configuración de colores (si colorama no está disponible, usa colores básicos)
try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)  # Resetea colores automáticamente
    COLORS_AVAILABLE = True
except ImportError:
    print("⚠️  Colorama no está instalado. Para colores ejecuta: pip install colorama")
    # Fallback sin colores
    class MockColor:
        def __getattr__(self, name):
            return ""
    Fore = Back = Style = MockColor()
    COLORS_AVAILABLE = False

class ColorPalette:
    """Paleta de colores para la cafetería"""
    # Colores principales
    HEADER = Fore.MAGENTA + Style.BRIGHT
    CAT_NAME = Fore.YELLOW + Style.BRIGHT
    SPACE_NAME = Fore.CYAN + Style.BRIGHT
    SUCCESS = Fore.GREEN + Style.BRIGHT
    WARNING = Fore.YELLOW
    ERROR = Fore.RED + Style.BRIGHT
    INFO = Fore.BLUE
    RESET = Style.RESET_ALL
    
    # Colores temáticos
    ENERGY = Fore.GREEN
    HUNGER = Fore.YELLOW
    MOOD = Fore.MAGENTA
    
    # Decoraciones
    SEPARATOR = Fore.WHITE + Style.DIM

class CatMood(Enum):
    """Estados de ánimo de los gatos"""
    FELIZ = "😸"
    CANSADO = "😴" 
    HAMBRIENTO = "🙀"
    JUGUETON = "😺"
    ENFERMO = "😿"
    NORMAL = "😐"

class CatBreed(Enum):
    """Razas de gatos disponibles"""
    PERSA = {"emoji": "🐱", "energy_bonus": 5, "hunger_bonus": 0}
    SIAMES = {"emoji": "🐈", "energy_bonus": 10, "hunger_bonus": -5}
    MAINE_COON = {"emoji": "🦁", "energy_bonus": 0, "hunger_bonus": 10}
    ESFINGE = {"emoji": "👽", "energy_bonus": 15, "hunger_bonus": -10}
    BENGALI = {"emoji": "🐅", "energy_bonus": 20, "hunger_bonus": -15}

class Gato:
    """Clase mejorada para representar un gato de cafetería"""
    
    def __init__(self, nombre, edad, lvl_energia=100, lvl_hambre=100, raza=None):
        self.nombre = str(nombre)
        self.edad = int(edad)
        self.lvl_energia = max(0, min(100, int(lvl_energia)))
        self.lvl_hambre = max(0, min(100, int(lvl_hambre)))
        self.raza = raza or random.choice(list(CatBreed))
        self.veces_jugado = 0
        self.veces_comido = 0
        self.tiempo_creacion = time.time()
        self.esta_enfermo = False
        
        # Aplicar bonos de raza
        breed_data = self.raza.value
        self.lvl_energia = min(100, self.lvl_energia + breed_data["energy_bonus"])
        self.lvl_hambre = min(100, self.lvl_hambre + breed_data["hunger_bonus"])

    @property
    def estado_animo(self):
        """Determina el estado de ánimo basado en estadísticas"""
        if self.esta_enfermo:
            return CatMood.ENFERMO
        elif self.lvl_energia < 20:
            return CatMood.CANSADO
        elif self.lvl_hambre < 30:
            return CatMood.HAMBRIENTO
        elif self.lvl_energia > 80 and self.lvl_hambre > 70:
            return CatMood.JUGUETON
        elif self.lvl_energia > 60 and self.lvl_hambre > 60:
            return CatMood.FELIZ
        else:
            return CatMood.NORMAL

    def get_barra_estado(self, valor, color, simbolo="█"):
        """Crea una barra de estado visual"""
        barras_llenas = valor // 10
        barra = color + simbolo * barras_llenas + Style.DIM + "░" * (10 - barras_llenas) + ColorPalette.RESET
        return f"{barra} {valor:3d}%"

    def cats_playing(self, intensidad="normal"):
        """Gato jugando con diferentes intensidades"""
        if self.esta_enfermo:
            self._print_cat_message(f"está muy enfermo para jugar", ColorPalette.ERROR)
            return False
            
        if self.lvl_energia < 10:
            self._print_cat_message(f"está demasiado cansado para jugar", ColorPalette.WARNING)
            return False

        # Determinar pérdida según intensidad
        intensidades = {
            "suave": (3, 2),
            "normal": (5, 5), 
            "intensa": (8, 7)
        }
        
        perdida_energia, perdida_hambre = intensidades.get(intensidad, intensidades["normal"])
        
        # Aplicar cambios
        self.lvl_energia = max(0, self.lvl_energia - perdida_energia)
        self.lvl_hambre = max(0, self.lvl_hambre - perdida_hambre)
        self.veces_jugado += 1
        
        # Posibilidad de enfermarse si juega demasiado
        if self.veces_jugado > 5 and random.random() < 0.1:
            self.esta_enfermo = True
            
        self._mostrar_actividad("jugando", intensidad)
        return True

    def cat_eating(self, tipo_comida="normal"):
        """Gato comiendo con diferentes tipos de comida"""
        if self.lvl_hambre >= 95:
            self._print_cat_message(f"está muy lleno y no quiere comer", ColorPalette.INFO)
            return False

        # Tipos de comida con diferentes efectos
        comidas = {
            "basica": (5, 3),
            "normal": (8, 5),
            "premium": (12, 8),
            "medicina": (5, 5)  # También cura enfermedades
        }
        
        ganancia_hambre, ganancia_energia = comidas.get(tipo_comida, comidas["normal"])
        
        # Aplicar cambios
        self.lvl_energia = min(100, self.lvl_energia + ganancia_energia)
        self.lvl_hambre = min(100, self.lvl_hambre + ganancia_hambre)
        self.veces_comido += 1
        
        # La medicina cura enfermedades
        if tipo_comida == "medicina":
            self.esta_enfermo = False
            self._print_cat_message(f"se siente mejor después de la medicina", ColorPalette.SUCCESS)
        
        self._mostrar_actividad("comiendo", tipo_comida)
        return True

    def descansar(self):
        """Gato descansando para recuperar energía"""
        if self.lvl_energia >= 95:
            self._print_cat_message(f"ya está muy descansado", ColorPalette.INFO)
            return False
            
        ganancia = random.randint(15, 25)
        self.lvl_energia = min(100, self.lvl_energia + ganancia)
        
        # El descanso puede curar enfermedades leves
        if self.esta_enfermo and random.random() < 0.3:
            self.esta_enfermo = False
            self._print_cat_message(f"se recuperó de su enfermedad descansando", ColorPalette.SUCCESS)
            
        self._mostrar_actividad("descansando")
        return True

    def _print_cat_message(self, mensaje, color=ColorPalette.INFO):
        """Imprime un mensaje del gato con formato"""
        emoji = self.raza.value["emoji"]
        print(f"{emoji} {ColorPalette.CAT_NAME}{self.nombre}{ColorPalette.RESET} {color}{mensaje}{ColorPalette.RESET}")

    def _mostrar_actividad(self, actividad, tipo=None):
        """Muestra la actividad del gato con estadísticas"""
        tipo_text = f" ({tipo})" if tipo else ""
        self._print_cat_message(f"está {actividad}{tipo_text}", ColorPalette.SUCCESS)
        print(f"   {ColorPalette.ENERGY}Energía: {self.get_barra_estado(self.lvl_energia, ColorPalette.ENERGY)}")
        print(f"   {ColorPalette.HUNGER}Hambre:  {self.get_barra_estado(self.lvl_hambre, ColorPalette.HUNGER)}")
        print(f"   Estado: {self.estado_animo.value} {self.estado_animo.name}")

    def get_tiempo_vida(self):
        """Tiempo que lleva el gato en la cafetería"""
        segundos = int(time.time() - self.tiempo_creacion)
        return f"{segundos}s"

    def __str__(self):
        emoji = self.raza.value["emoji"]
        raza_name = self.raza.name.replace("_", " ").title()
        estado = self.estado_animo.value
        
        return (f"{emoji} {ColorPalette.CAT_NAME}{self.nombre}{ColorPalette.RESET} "
                f"({raza_name}, {self.edad} años) {estado} | "
                f"{ColorPalette.ENERGY}E:{self.lvl_energia:3d}{ColorPalette.RESET} "
                f"{ColorPalette.HUNGER}H:{self.lvl_hambre:3d}{ColorPalette.RESET}")

    def __del__(self):
        razon = "se escapó" if not self.esta_enfermo else "fue al veterinario"
        print(f"{ColorPalette.WARNING}🚪 El gato {self.nombre} {razon} de la cafetería{ColorPalette.RESET}")

class EspacioCafe:
    """Clase mejorada para los espacios de la cafetería"""
    
    TIPOS_ESPACIOS = {
        "cocina": {"emoji": "🍳", "actividades": ["comiendo"]},
        "sala_juegos": {"emoji": "🎮", "actividades": ["jugando"]},
        "dormitorio": {"emoji": "🛏️", "actividades": ["descansando"]},
        "hall": {"emoji": "🏛️", "actividades": ["jugando", "descansando"]},
        "terraza": {"emoji": "🌿", "actividades": ["jugando", "comiendo", "descansando"]},
        "enfermeria": {"emoji": "🏥", "actividades": ["medicina"]}
    }
    
    def __init__(self, nombre_espacio, capacidad_maxima, tipo_espacio="hall"):
        self.nombre_espacio = str(nombre_espacio)
        self.capacidad_maxima = int(capacidad_maxima)
        self.tipo_espacio = tipo_espacio
        self.gatos_en_espacio = []
        self.actividades_disponibles = self.TIPOS_ESPACIOS.get(tipo_espacio, self.TIPOS_ESPACIOS["hall"])

    def mover_gato(self, gato):
        """Mueve un gato al espacio"""
        if len(self.gatos_en_espacio) >= self.capacidad_maxima:
            print(f"{ColorPalette.ERROR}❌ ¡Espacio lleno en {self._get_formatted_name()}!{ColorPalette.RESET}")
            return False
        
        if gato in self.gatos_en_espacio:
            print(f"{ColorPalette.WARNING}⚠️  {gato.nombre} ya está en {self._get_formatted_name()}{ColorPalette.RESET}")
            return False
            
        self.gatos_en_espacio.append(gato)
        emoji = self.actividades_disponibles["emoji"]
        print(f"{ColorPalette.SUCCESS}✅ {emoji} {gato.nombre} entró a {self._get_formatted_name()}{ColorPalette.RESET}")
        return True

    def remover_gato(self, gato):
        """Remueve un gato del espacio"""
        if gato not in self.gatos_en_espacio:
            print(f"{ColorPalette.ERROR}❌ {gato.nombre} no está en {self._get_formatted_name()}{ColorPalette.RESET}")
            return False
            
        self.gatos_en_espacio.remove(gato)
        print(f"{ColorPalette.INFO}🚪 {gato.nombre} salió de {self._get_formatted_name()}{ColorPalette.RESET}")
        return True

    def actividad_grupal(self):
        """Realiza una actividad grupal en el espacio"""
        if not self.gatos_en_espacio:
            print(f"{ColorPalette.WARNING}😿 No hay gatos en {self._get_formatted_name()} para actividades{ColorPalette.RESET}")
            return
            
        actividad = random.choice(self.actividades_disponibles["actividades"])
        print(f"\n{ColorPalette.HEADER}🎪 ¡ACTIVIDAD GRUPAL en {self._get_formatted_name()}: {actividad.upper()}!{ColorPalette.RESET}")
        
        for gato in self.gatos_en_espacio:
            if actividad == "jugando":
                gato.cats_playing(random.choice(["suave", "normal", "intensa"]))
            elif actividad == "comiendo":
                gato.cat_eating(random.choice(["normal", "premium"]))
            elif actividad == "descansando":
                gato.descansar()
            elif actividad == "medicina":
                gato.cat_eating("medicina")
            time.sleep(0.5)  # Pequeña pausa para efecto visual

    def _get_formatted_name(self):
        """Nombre formateado del espacio"""
        emoji = self.actividades_disponibles["emoji"]
        return f"{emoji} {ColorPalette.SPACE_NAME}{self.nombre_espacio}{ColorPalette.RESET}"

    def info_espacio(self):
        """Muestra información detallada del espacio"""
        ocupacion = len(self.gatos_en_espacio)
        porcentaje = (ocupacion / self.capacidad_maxima) * 100
        
        # Colores según ocupación
        color_ocupacion = ColorPalette.SUCCESS if porcentaje < 70 else ColorPalette.WARNING if porcentaje < 100 else ColorPalette.ERROR
        
        print(f"\n{ColorPalette.SEPARATOR}{'='*50}{ColorPalette.RESET}")
        print(f"{self._get_formatted_name()}")
        print(f"{color_ocupacion}Ocupación: {ocupacion}/{self.capacidad_maxima} ({porcentaje:.0f}%){ColorPalette.RESET}")
        print(f"Actividades: {', '.join(self.actividades_disponibles['actividades'])}")
        
        if self.gatos_en_espacio:
            print(f"\n{ColorPalette.INFO}🐱 Gatos presentes:{ColorPalette.RESET}")
            for i, gato in enumerate(self.gatos_en_espacio, 1):
                print(f"   {i}. {gato}")
        else:
            print(f"{ColorPalette.WARNING}😿 No hay gatos en este espacio{ColorPalette.RESET}")

class CafeteriaManager:
    """Administrador principal de la cafetería"""
    
    def __init__(self, nombre_cafeteria="🐱 Cat Café Paradise"):
        self.nombre = nombre_cafeteria
        self.gatos = []
        self.espacios = []
        self.tiempo_inicio = time.time()

    def agregar_gato(self, gato):
        """Agrega un gato a la cafetería"""
        self.gatos.append(gato)
        print(f"{ColorPalette.SUCCESS}🎉 ¡Bienvenido {gato.nombre} a la cafetería!{ColorPalette.RESET}")

    def agregar_espacio(self, espacio):
        """Agrega un espacio a la cafetería"""
        self.espacios.append(espacio)

    def resumen_general(self):
        """Muestra un resumen completo de la cafetería"""
        tiempo_operacion = int(time.time() - self.tiempo_inicio)
        
        print(f"\n{ColorPalette.HEADER}{'='*60}")
        print(f"📊 RESUMEN DE {self.nombre}")
        print(f"{'='*60}{ColorPalette.RESET}")
        print(f"⏱️  Tiempo de operación: {tiempo_operacion}s")
        print(f"🐱 Total de gatos: {len(self.gatos)}")
        print(f"🏠 Espacios disponibles: {len(self.espacios)}")
        
        # Estadísticas de gatos
        if self.gatos:
            energia_promedio = sum(g.lvl_energia for g in self.gatos) / len(self.gatos)
            hambre_promedio = sum(g.lvl_hambre for g in self.gatos) / len(self.gatos)
            gatos_enfermos = sum(1 for g in self.gatos if g.esta_enfermo)
            
            print(f"\n📈 Estadísticas:")
            print(f"   Energía promedio: {ColorPalette.ENERGY}{energia_promedio:.1f}%{ColorPalette.RESET}")
            print(f"   Hambre promedio: {ColorPalette.HUNGER}{hambre_promedio:.1f}%{ColorPalette.RESET}")
            print(f"   Gatos enfermos: {ColorPalette.ERROR}{gatos_enfermos}{ColorPalette.RESET}")

        # Mostrar todos los espacios
        print(f"\n{ColorPalette.INFO}🏠 Estado de los espacios:{ColorPalette.RESET}")
        for espacio in self.espacios:
            espacio.info_espacio()

    def simulacion_automatica(self, duracion_segundos=10):
        """Ejecuta una simulación automática"""
        print(f"\n{ColorPalette.HEADER}🎬 INICIANDO SIMULACIÓN AUTOMÁTICA ({duracion_segundos}s){ColorPalette.RESET}")
        
        tiempo_fin = time.time() + duracion_segundos
        
        while time.time() < tiempo_fin:
            # Actividad aleatoria
            if self.espacios:
                espacio_aleatorio = random.choice(self.espacios)
                espacio_aleatorio.actividad_grupal()
            
            # Mover gatos aleatoriamente
            if self.gatos and len(self.gatos) > 1:
                gato = random.choice(self.gatos)
                espacio_actual = None
                
                # Encontrar espacio actual del gato
                for esp in self.espacios:
                    if gato in esp.gatos_en_espacio:
                        espacio_actual = esp
                        break
                
                # Mover a nuevo espacio
                if espacio_actual:
                    espacio_actual.remover_gato(gato)
                
                nuevo_espacio = random.choice(self.espacios)
                nuevo_espacio.mover_gato(gato)
            
            time.sleep(2)  # Pausa entre actividades
        
        print(f"{ColorPalette.SUCCESS}✅ Simulación completada{ColorPalette.RESET}")

# ================================
# PROGRAMA PRINCIPAL
# ================================

def main():
    """Función principal mejorada"""
    print(f"{ColorPalette.HEADER}")
    print("🐱" * 20)
    print("  CAFETERÍA DE GATOS PREMIUM")  
    print("🐱" * 20)
    print(f"{ColorPalette.RESET}")
    
    # Crear el manager de la cafetería
    cafeteria = CafeteriaManager()
    
    # Crear gatos con razas aleatorias
    nombres_gatos = ["Piskolita", "Roun", "Cervei", "Dimitri", "Vodki", "Kurvi", "Luna", "Milo"]
    for nombre in nombres_gatos:
        edad = random.randint(1, 8)
        energia = random.randint(70, 100)
        hambre = random.randint(60, 100)
        raza = random.choice(list(CatBreed))
        
        gato = Gato(nombre, edad, energia, hambre, raza)
        cafeteria.agregar_gato(gato)
    
    # Crear espacios temáticos
    espacios_config = [
        ("Cocina Principal", 3, "cocina"),
        ("Sala de Juegos", 4, "sala_juegos"), 
        ("Dormitorio Felino", 6, "dormitorio"),
        ("Hall Central", 8, "hall"),
        ("Terraza Soleada", 5, "terraza"),
        ("Enfermería", 2, "enfermeria")
    ]
    
    for nombre, capacidad, tipo in espacios_config:
        espacio = EspacioCafe(nombre, capacidad, tipo)
        cafeteria.agregar_espacio(espacio)
    
    # Distribuir gatos inicialmente
    print(f"\n{ColorPalette.INFO}🏠 Distribuyendo gatos en los espacios...{ColorPalette.RESET}")
    for gato in cafeteria.gatos[:6]:  # Solo los primeros 6
        espacio = random.choice(cafeteria.espacios)
        espacio.mover_gato(gato)
    
    # Mostrar estado inicial
    cafeteria.resumen_general()
    
    # Realizar algunas actividades manuales
    print(f"\n{ColorPalette.HEADER}🎮 ACTIVIDADES MANUALES{ColorPalette.RESET}")
    
    # Actividades específicas
    if cafeteria.gatos:
        gato1 = cafeteria.gatos[0]
        gato1.cats_playing("intensa")
        time.sleep(1)
        gato1.cat_eating("premium")
        time.sleep(1)
        gato1.descansar()
    
    # Actividades grupales
    if cafeteria.espacios:
        cafeteria.espacios[0].actividad_grupal()
        time.sleep(2)
        cafeteria.espacios[1].actividad_grupal()
    
    # Ejecutar simulación automática
    cafeteria.simulacion_automatica(5)
    
    # Resumen final
    cafeteria.resumen_general()
    
    # Demostrar destructores
    print(f"\n{ColorPalette.WARNING}👋 Los gatos se van de la cafetería...{ColorPalette.RESET}")
    del cafeteria.gatos[0]  # Eliminar un gato para ver el destructor
    
    print(f"\n{ColorPalette.SUCCESS}✨ ¡Gracias por visitar nuestra cafetería! ✨{ColorPalette.RESET}")

if __name__ == "__main__":
    main()