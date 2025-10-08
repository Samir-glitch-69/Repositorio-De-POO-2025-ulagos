class Membresia:
    """
    Clase para gestionar membresías del gimnasio Energy.
    Permite controlar planes (Diario, Pase10, Ilimitado), créditos y accesos.
    """
    
    # Variables de clase (sugeridas)
    TARIFAS_MEMBRESIAS = {
        "Diario": 0,
        "Pase10": 10,
        "Ilimitado": 0
    }
    __creadas = 0  # Contador global de membresías creadas (privado)
    
    def __init__(self, nombre: str, plan: str):
        """
        Inicializa una membresía. Pre: plan válido (Diario, Pase10, Ilimitado)
        """
        # Validar que el plan sea válido
        if not Membresia.es_plan_valido(plan):
            raise ValueError(f"Plan inválido: {plan}. Debe ser Diario, Pase10 o Ilimitado")
        
        # Atributos privados (encapsulación)
        self.__nombre = nombre
        self.__plan = plan
        self.__activa = True
        
        # Inicializar créditos según el plan
        if plan == "Pase10":
            self.__creditos = 10  # No negativos según requisitos
        else:
            self.__creditos = 0
        
        # Incrementar contador global
        Membresia.__creadas += 1
    
    def __str__(self) -> str:
        """Devuelve una representación legible del objeto"""
        estado = "Activa" if self.__activa else "Inactiva"
        return f"Membresía({self.__nombre}, Plan: {self.__plan}, Créditos: {self.__creditos}, Estado: {estado})"
    
    def __repr__(self) -> str:
        """Representación técnica del objeto"""
        return f"Membresia(nombre='{self.__nombre}', plan='{self.__plan}')"
    
    # Métodos estáticos
    @staticmethod
    def es_plan_valido(plan: str) -> bool:
        """
        Retorna True si el plan es válido: Diario, Pase10, Ilimitado
        """
        return plan in ["Diario", "Pase10", "Ilimitado"]
    
    # Métodos de clase
    @classmethod
    def total_creadas(cls) -> int:
        """
        Retorna el total de membresías creadas (contador global)
        """
        return cls.__creadas
    
    # Properties (getters) - Exponer solo lo necesario
    @property
    def nombre(self) -> str:
        """Obtiene el nombre del miembro"""
        return self.__nombre
    
    @property
    def plan(self) -> str:
        """Obtiene el plan actual"""
        return self.__plan
    
    @property
    def creditos(self) -> int:
        """Obtiene los créditos (solo lectura)"""
        return self.__creditos
    
    @property
    def activa(self) -> bool:
        """Verifica si la membresía está activa"""
        return self.__activa
    
    # Setter para plan (con validaciones - invariantes)
    @plan.setter
    def plan(self, nuevo_plan: str):
        """
        Cambia el plan. Pre: membresía activa y plan válido
        Postcondición: Si cambia a Pase10, inicializa con 10 créditos
        """
        if not self.__activa:
            raise ValueError("No se puede cambiar el plan de una membresía inactiva")
        
        if not Membresia.es_plan_valido(nuevo_plan):
            raise ValueError(f"Plan inválido: {nuevo_plan}")
        
        self.__plan = nuevo_plan
        
        # Si cambia a Pase10, inicializar créditos (Postcondición)
        if nuevo_plan == "Pase10":
            self.__creditos = 10
        else:
            self.__creditos = 0
    
    # Métodos principales
    def registrar_asistencia(self) -> bool:
        """
        Registra un acceso. Pre: membresía activa
        a. Requiere membresía activa
        b. Si es Pase10, necesita créditos > 0 y descuenta 1
        c. Si es Diario o Ilimitado, permite el acceso sin usar créditos
        d. Retorna True si el acceso fue registrado, False en caso contrario
        """
        # a. Verificar que la membresía esté activa
        if not self.__activa:
            return False
        
        # b. Si es Pase10, verificar créditos y descontar
        if self.__plan == "Pase10":
            if self.__creditos > 0:
                self.__creditos -= 1
                return True
            else:
                return False  # Sin créditos
        
        # c. Si es Diario o Ilimitado, permitir acceso sin usar créditos
        elif self.__plan in ["Diario", "Ilimitado"]:
            return True
        
        return False
    
    def congelar(self) -> None:
        """
        Inactiva la membresía
        """
        self.__activa = False
    
    def reactivar(self) -> None:
        """
        Reactiva la membresía
        """
        self.__activa = True
    
    def agregar_creditos(self, cantidad: int) -> None:
        """
        Agrega créditos a la membresía (solo para plan Pase10)
        Precondición: cantidad > 0
        """
        if cantidad <= 0:
            raise ValueError("La cantidad de créditos debe ser mayor a 0")
        
        if self.__plan == "Pase10":
            self.__creditos += cantidad
        else:
            print(f"Advertencia: No se pueden agregar créditos al plan {self.__plan}")


# ===== CÓDIGO DE PRUEBA =====
def pruebas():
    """Función para probar la clase Membresia"""
    print("=" * 60)
    print("SISTEMA DE GESTIÓN DE MEMBRESÍAS - GIMNASIO ENERGY")
    print("=" * 60)
    
    # Prueba 1: Crear membresías con diferentes planes
    print("\n1. CREACIÓN DE MEMBRESÍAS:")
    print("-" * 60)
    m1 = Membresia("Juan Pérez", "Diario")
    m2 = Membresia("María López", "Pase10")
    m3 = Membresia("Carlos Ruiz", "Ilimitado")
    
    print(m1)
    print(m2)
    print(m3)
    print(f"\nTotal de membresías creadas: {Membresia.total_creadas()}")
    
    # Prueba 2: Registrar asistencias
    print("\n2. REGISTRO DE ASISTENCIAS:")
    print("-" * 60)
    
    # Diario - debe permitir siempre
    print(f"Juan (Diario) registra asistencia: {m1.registrar_asistencia()}")
    print(f"Juan (Diario) registra asistencia: {m1.registrar_asistencia()}")
    
    # Pase10 - debe descontar créditos
    print(f"\nMaría (Pase10) créditos iniciales: {m2.creditos}")
    for i in range(3):
        resultado = m2.registrar_asistencia()
        print(f"María registra asistencia #{i+1}: {resultado}, Créditos restantes: {m2.creditos}")
    
    # Ilimitado - debe permitir siempre
    print(f"\nCarlos (Ilimitado) registra asistencia: {m3.registrar_asistencia()}")
    print(f"Carlos (Ilimitado) registra asistencia: {m3.registrar_asistencia()}")
    
    # Prueba 3: Agotar créditos en Pase10
    print("\n3. PRUEBA DE AGOTAMIENTO DE CRÉDITOS:")
    print("-" * 60)
    m4 = Membresia("Ana Torres", "Pase10")
    print(f"Ana (Pase10) créditos iniciales: {m4.creditos}")
    
    for i in range(12):  # Intentar más de 10 accesos
        resultado = m4.registrar_asistencia()
        print(f"Acceso #{i+1}: {'✓ Permitido' if resultado else '✗ Denegado'} - Créditos: {m4.creditos}")
    
    # Prueba 4: Congelar y reactivar
    print("\n4. CONGELAR Y REACTIVAR MEMBRESÍA:")
    print("-" * 60)
    print(f"Estado de Juan: {'Activa' if m1.activa else 'Inactiva'}")
    print("Congelando membresía...")
    m1.congelar()
    print(f"Estado de Juan: {'Activa' if m1.activa else 'Inactiva'}")
    print(f"¿Puede registrar asistencia?: {m1.registrar_asistencia()}")
    
    print("\nReactivando membresía...")
    m1.reactivar()
    print(f"Estado de Juan: {'Activa' if m1.activa else 'Inactiva'}")
    print(f"¿Puede registrar asistencia?: {m1.registrar_asistencia()}")
    
    # Prueba 5: Cambiar plan
    print("\n5. CAMBIO DE PLAN:")
    print("-" * 60)
    print(f"Plan actual de María: {m2.plan}, Créditos: {m2.creditos}")
    print("Cambiando a plan Ilimitado...")
    m2.plan = "Ilimitado"
    print(f"Nuevo plan de María: {m2.plan}, Créditos: {m2.creditos}")
    
    print("\nCambiando de nuevo a Pase10...")
    m2.plan = "Pase10"
    print(f"Plan de María: {m2.plan}, Créditos: {m2.creditos} (se reinician a 10)")
    
    # Prueba 6: Agregar créditos
    print("\n6. AGREGAR CRÉDITOS:")
    print("-" * 60)
    m5 = Membresia("Pedro Gómez", "Pase10")
    print(f"Pedro (Pase10) créditos iniciales: {m5.creditos}")
    m5.agregar_creditos(5)
    print(f"Después de agregar 5 créditos: {m5.creditos}")
    
    # Prueba 7: Validaciones
    print("\n7. PRUEBAS DE VALIDACIÓN:")
    print("-" * 60)
    try:
        m_invalida = Membresia("Usuario Test", "PlanInvalido")
    except ValueError as e:
        print(f"✓ Error capturado correctamente: {e}")
    
    try:
        m1.congelar()
        m1.plan = "Pase10"  # Intentar cambiar plan estando inactiva
    except ValueError as e:
        print(f"✓ Error capturado correctamente: {e}")
    finally:
        m1.reactivar()  # Reactivar para otras pruebas
    
    # Prueba 8: Método estático
    print("\n8. VALIDACIÓN DE PLANES:")
    print("-" * 60)
    planes_prueba = ["Diario", "Pase10", "Ilimitado", "Mensual", ""]
    for plan in planes_prueba:
        valido = Membresia.es_plan_valido(plan)
        print(f"Plan '{plan}': {'✓ Válido' if valido else '✗ Inválido'}")
    
    print("\n" + "=" * 60)
    print(f"TOTAL DE MEMBRESÍAS CREADAS: {Membresia.total_creadas()}")
    print("=" * 60)


if __name__ == "__main__":
    pruebas()