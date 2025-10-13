# ============================================================================
# EJEMPLOS COMPLETOS DE CONCEPTOS POO EN PYTHON
# ============================================================================

# ============================================================================
# EJEMPLO 1: CLASE BÁSICA CON TODOS LOS CONCEPTOS
# ============================================================================

class Persona:
    """
    Clase que demuestra todos los conceptos de POO:
    - assert
    - @staticmethod
    - @property
    - @property.setter
    - None
    - Anotaciones de tipo (parametro: tipo, -> tipo)
    """
    
    # Variable de clase (compartida por todas las instancias)
    contador_personas = 0
    
    def __init__(self, nombre: str, edad: int):
        """
        Constructor de la clase.
        Precondición: edad debe ser >= 0
        """
        # assert: validar que edad sea válida
        assert edad >= 0, "La edad no puede ser negativa"
        assert isinstance(nombre, str), "El nombre debe ser un string"
        
        # Atributos privados (encapsulación)
        self.__nombre = nombre
        self.__edad = edad
        self.__activo = True
        
        # Incrementar contador de clase
        Persona.contador_personas += 1
    
    def __str__(self) -> str:
        """Método mágico para representación legible"""
        estado = "Activo" if self.__activo else "Inactivo"
        return f"Persona: {self.__nombre}, {self.__edad} años, Estado: {estado}"
    
    # ========== @staticmethod ==========
    @staticmethod
    def es_mayor_edad(edad: int) -> bool:
        """
        Método estático: NO necesita self ni cls
        Verifica si una edad corresponde a mayor de edad
        """
        return edad >= 18
    
    @staticmethod
    def validar_nombre(nombre: str) -> bool:
        """Valida que el nombre tenga al menos 2 caracteres"""
        return len(nombre) >= 2
    
    # ========== @classmethod ==========
    @classmethod
    def total_personas(cls) -> int:
        """
        Método de clase: accede a variables de clase
        Retorna el total de personas creadas
        """
        return cls.contador_personas
    
    # ========== @property (GETTERS) ==========
    @property
    def nombre(self) -> str:
        """Obtiene el nombre (solo lectura desde afuera)"""
        return self.__nombre
    
    @property
    def edad(self) -> int:
        """Obtiene la edad (solo lectura)"""
        return self.__edad
    
    @property
    def activo(self) -> bool:
        """Obtiene el estado de activación"""
        return self.__activo
    
    # ========== @property.setter (SETTERS) ==========
    @edad.setter
    def edad(self, nueva_edad: int) -> None:
        """
        Modifica la edad con validación.
        -> None indica que no retorna nada
        """
        # Validar antes de asignar
        assert nueva_edad >= 0, "La edad no puede ser negativa"
        assert nueva_edad <= 150, "La edad no puede ser mayor a 150"
        
        self.__edad = nueva_edad
        print(f"Edad actualizada a {nueva_edad}")
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        """Modifica el nombre con validación"""
        assert len(nuevo_nombre) >= 2, "El nombre debe tener al menos 2 caracteres"
        self.__nombre = nuevo_nombre
        print(f"Nombre actualizado a {nuevo_nombre}")
    
    # ========== Métodos que retornan None ==========
    def activar(self) -> None:
        """Activa la persona. No retorna nada."""
        self.__activo = True
        print(f"{self.__nombre} ha sido activado")
    
    def desactivar(self) -> None:
        """Desactiva la persona. No retorna nada."""
        self.__activo = False
        print(f"{self.__nombre} ha sido desactivado")
    
    def saludar(self) -> None:
        """Imprime un saludo. No retorna nada."""
        print(f"Hola, soy {self.__nombre} y tengo {self.__edad} años")
    
    # ========== Métodos que SÍ retornan valores ==========
    def es_adulto(self) -> bool:
        """Retorna True si es mayor de edad"""
        return self.__edad >= 18
    
    def años_hasta_jubilacion(self) -> int:
        """Calcula años hasta la jubilación (65 años)"""
        if self.__edad >= 65:
            return 0
        return 65 - self.__edad 