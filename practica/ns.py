class Membresia:
    """
    Clase que representa una membresía del gimnasio Energy.
    Gestiona planes (Diario, Pase10, Ilimitado), créditos y estado de activación.
    """
    
    # Variables de clase
    TARIFAS_MEMBRESIAS = {
        "Diario": 5000,
        "Pase10": 35000,
        "Ilimitado": 50000
    }
    _creadas = 0  # Contador global de membresías creadas
    
    def __init__(self, nombre: str, plan: str):
        """
        Inicializa una membresía.
        Precondición: plan debe ser válido (Diario, Pase10, o Ilimitado)
        Postcondición: membresía creada activa con créditos según el plan
        """
        # Verificar precondición
        if not self.es_plan_valido(plan):
            raise ValueError(f"Plan '{plan}' no es válido. Debe ser: Diario, Pase10 o Ilimitado")
        
        # Atributos privados (encapsulación)
        self.__nombre = nombre
        self.__plan = plan
        self.__activa = True  # Por defecto, inicia activa
        
        # Asignar créditos según el plan
        if plan == "Pase10":
            self.__creditos = 10
        else:
            self.__creditos = 0  # Diario e Ilimitado no usan créditos
        
        # Incrementar contador global
        Membresia._creadas += 1
        
        # Verificar invariante
        self._verificar_invariante()
    
    def _verificar_invariante(self):
        """
        Verifica las invariantes de la clase:
        - El plan debe ser válido
        - Los créditos no deben ser negativos
        - Si el plan es Pase10, debe tener créditos definidos
        """
        assert self.es_plan_valido(self.__plan), "Invariante violada: plan inválido"
        assert self.__creditos >= 0, "Invariante violada: créditos negativos"
        if self.__plan == "Pase10":
            assert self.__creditos >= 0, "Invariante violada: Pase10 sin créditos válidos"
    
    def __str__(self) -> str:
        """Devuelve una representación legible del objeto"""
        estado = "Activa" if self.__activa else "Congelada"
        creditos_info = f", Créditos: {self.__creditos}" if self.__plan == "Pase10" else ""
        return f"Membresía de {self.__nombre} - Plan: {self.__plan} - Estado: {estado}{creditos_info}"
    
    def __repr__(self) -> str:
        """Representación técnica del objeto"""
        return f"Membresia(nombre='{self.__nombre}', plan='{self.__plan}', activa={self.__activa}, creditos={self.__creditos})"
    
    @staticmethod
    def es_plan_valido(plan: str) -> bool:
        """
        Retorna True si el plan es válido: Diario, Pase10, Ilimitado
        Método estático porque no depende del estado de la instancia
        """
        return plan in ["Diario", "Pase10", "Ilimitado"]
    
    @classmethod
    def total_creadas(cls) -> int:
        """
        Retorna el total de membresías creadas (contador global)
        Método de clase porque accede a una variable de clase
        """
        return cls._creadas
    
    @property
    def plan(self) -> str:
        """Obtiene el plan actual (solo lectura a través del getter)"""
        return self.__plan
    
    @plan.setter
    def plan(self, nuevo_plan: str):
        """
        Cambia el plan de la membresía.
        Precondición: membresía debe estar activa y el plan debe ser válido
        Postcondición: plan actualizado y créditos ajustados según corresponda
        """
        # Verificar precondiciones
        if not self.__activa:
            raise ValueError("No se puede cambiar el plan de una membresía congelada")
        
        if not self.es_plan_valido(nuevo_plan):
            raise ValueError(f"Plan '{nuevo_plan}' no es válido")
        
        # Cambiar el plan
        self.__plan = nuevo_plan
        
        # Ajustar créditos según el nuevo plan
        if nuevo_plan == "Pase10":
            self.__creditos = 10  # Renovar créditos
        else:
            self.__creditos = 0  # Diario e Ilimitado no usan créditos
        
        # Verificar invariante
        self._verificar_invariante()
    
    @property
    def creditos(self) -> int:
        """Obtiene los créditos actuales (solo lectura)"""
        return self.__creditos
    
    @property
    def nombre(self) -> str:
        """Obtiene el nombre del titular (solo lectura)"""
        return self.__nombre
    
    @property
    def activa(self) -> bool:
        """Obtiene el estado de activación (solo lectura)"""
        return self.__activa
    
    def registrar_asistencia(self) -> bool:
        """
        Registra un acceso al gimnasio.
        Precondición: membresía debe estar activa
        Retorna True si se registra el acceso; False en caso contrario
        Postcondición: si es Pase10, créditos decrementados en 1
        """
        # Verificar precondición: membresía activa
        if not self.__activa:
            print(f"Acceso denegado: La membresía de {self.__nombre} está congelada")
            return False
        
        # Lógica según el tipo de plan
        if self.__plan == "Pase10":
            if self.__creditos > 0:
                self.__creditos -= 1
                print(f"Acceso registrado para {self.__nombre}. Créditos restantes: {self.__creditos}")
                self._verificar_invariante()
                return True
            else:
                print(f"Acceso denegado: {self.__nombre} no tiene créditos disponibles")
                return False
        
        elif self.__plan == "Diario":
            print(f"Acceso registrado para {self.__nombre} (Plan Diario)")
            return True
        
        elif self.__plan == "Ilimitado":
            print(f"Acceso registrado para {self.__nombre} (Plan Ilimitado)")
            return True
        
        return False
    
    def congelar(self) -> None:
        """
        Inactiva la membresía (congela la cuenta)
        Postcondición: membresía marcada como inactiva
        """
        if not self.__activa:
            print(f"La membresía de {self.__nombre} ya está congelada")
        else:
            self.__activa = False
            print(f"Membresía de {self.__nombre} congelada exitosamente")
    
    def reactivar(self) -> None:
        """
        Reactiva la membresía
        Postcondición: membresía marcada como activa
        """
        if self.__activa:
            print(f"La membresía de {self.__nombre} ya está activa")
        else:
            self.__activa = True
            print(f"Membresía de {self.__nombre} reactivada exitosamente")


# ==================== CÓDIGO DE PRUEBA ====================

def pruebas_sistema():
    """Función para probar el sistema de membresías"""
    
    print("=" * 60)
    print("PRUEBAS DEL SISTEMA DE MEMBRESÍAS - GIMNASIO ENERGY")
    print("=" * 60)
    
    # Prueba 1: Crear membresías
    print("\n--- PRUEBA 1: Creación de Membresías ---")
    m1 = Membresia("Juan Pérez", "Pase10")
    m2 = Membresia("María López", "Ilimitado")
    m3 = Membresia("Carlos Ruiz", "Diario")
    
    print(m1)
    print(m2)
    print(m3)
    print(f"\nTotal de membresías creadas: {Membresia.total_creadas()}")
    
    # Prueba 2: Registrar asistencias
    print("\n--- PRUEBA 2: Registro de Asistencias ---")
    m1.registrar_asistencia()  # Pase10: 9 créditos
    m1.registrar_asistencia()  # Pase10: 8 créditos
    m2.registrar_asistencia()  # Ilimitado: OK
    m3.registrar_asistencia()  # Diario: OK
    
    # Prueba 3: Agotar créditos
    print("\n--- PRUEBA 3: Agotar Créditos de Pase10 ---")
    for i in range(10):
        m1.registrar_asistencia()
    
    # Prueba 4: Congelar y reactivar
    print("\n--- PRUEBA 4: Congelar y Reactivar Membresía ---")
    m2.congelar()
    m2.registrar_asistencia()  # Debe fallar
    m2.reactivar()
    m2.registrar_asistencia()  # Debe funcionar
    
    # Prueba 5: Cambiar plan
    print("\n--- PRUEBA 5: Cambio de Plan ---")
    print(f"Plan actual de Juan: {m1.plan}")
    m1.plan = "Ilimitado"
    print(f"Nuevo plan de Juan: {m1.plan}")
    m1.registrar_asistencia()
    
    # Prueba 6: Intentar operaciones inválidas
    print("\n--- PRUEBA 6: Manejo de Errores ---")
    try:
        m_invalida = Membresia("Test", "PlanInvalido")
    except ValueError as e:
        print(f"Error capturado: {e}")
    
    m3.congelar()
    try:
        m3.plan = "Pase10"
    except ValueError as e:
        print(f"Error capturado: {e}")
    
    # Prueba 7: Validación de planes
    print("\n--- PRUEBA 7: Validación de Planes ---")
    print(f"¿'Diario' es válido? {Membresia.es_plan_valido('Diario')}")
    print(f"¿'Premium' es válido? {Membresia.es_plan_valido('Premium')}")
    
    print("\n" + "=" * 60)
    print("RESUMEN FINAL")
    print("=" * 60)
    print(f"Total de membresías creadas: {Membresia.total_creadas()}")
    print(m1)
    print(m2)
    print(m3)


# Ejecutar pruebas
if __name__ == "__main__":
    pruebas_sistema()