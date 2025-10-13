#ejercicio hecho por el profesor, el mio esta en el papel :p
class Membresia:
    
    # Variables Globales (fuera del constructor)
    PLANES_VALIDOS = {"DIARIO", "PASE_10", "ILIMITADO"}   # opciones de planes disponibles
    TARIFAS_MEMBRESIAS = {"DIARIO": 10990, "PASE_10": 20990, "ILIMITADO": 59900}  
    creadas = 0  # variable de clase contador global

    def __init__(self, nombre: str, plan: str):
        if not self.es_plan_valido(plan):
            raise ValueError("¡Plan Inválido!")
        self.__nombre = nombre
        self.__plan = plan
        self.__estado = True
        self.__creditos = 10 if plan == "PASE_10" else None
        Membresia.creadas += 1

    """NOTA: La flecha "-> str" indica que la salida esperada es un string.
    Es solo para la documentación y no cambia la ejecución. Ayuda a leer el código y a que herramientas
    como los IDE detecten errores de tipos. (su uso es opcional)"""

    def __str__(self) -> str:
        return f"Membresia (nombre={self.__nombre}, plan={self.__plan}, creditos={self.__creditos}, activo={self.__estado})"

    @staticmethod
    def es_plan_valido(plan: str) -> bool:
        return plan in Membresia.PLANES_VALIDOS

    @classmethod
    def total_creadas(cls) -> int:
        return cls.creadas

    @property
    def plan(self) -> str:
        return self.__plan

    @plan.setter
    def plan(self, nuevo_plan: str) -> None:
        if not self.__estado:
            raise ValueError("No se puede cambiar el plan estando inactiva")
        if nuevo_plan not in self.PLANES_VALIDOS:
            raise ValueError("¡Plan inválido!")

        # LÓGICA DIFERENCIADA POR PLAN
        if nuevo_plan == "PASE_10":
            self.__plan = "PASE_10"
            self.__creditos = 10
        elif nuevo_plan == "ILIMITADO":
            self.__plan = "ILIMITADO"
            self.__creditos = None
        else:  # DIARIO
            self.__plan = "DIARIO"
            self.__creditos = None

    @property
    def creditos(self):
        # solo lectura (no hay setter!!!)
        return self.__creditos

    def registrar_asistencia(self) -> bool:
        # Precondición: debe estar activa
        if not self.__estado:
            return False
        if self.__plan == "PASE_10":
            if self.__creditos is not None and self.__creditos > 0:
                self.__creditos -= 1
                return True
            return False
        # DIARIO o ILIMITADO: Acceso permitido
        return True

    def congelar(self) -> None:
        self.__estado = False

    def reactivar(self) -> None:
        self.__estado = True

# INSTANCIAS DE CLASES
membresia1 = Membresia("Anabell", "PASE_10")
membresia2 = Membresia("Constanza", "ILIMITADO")

print(membresia1)  # estado inicial
print(membresia2)
print("Total Creadas:", Membresia.total_creadas())

# Anabell entra 2 veces (PASE_10)
membresia1.registrar_asistencia()
membresia1.registrar_asistencia()
print("Créditos Anabell tras 3 accesos:", membresia1.creditos)

# Congelar y probar acceso
membresia1.congelar()
print("Intento acceso membresía congelada:", membresia1.registrar_asistencia())

# Reactivar y cambiar a DIARIO
membresia1.reactivar()
membresia1.plan = "DIARIO"
print(membresia1)
print("Intento acceso con el plan DIARIO:", membresia1.registrar_asistencia())
print(membresia1)
