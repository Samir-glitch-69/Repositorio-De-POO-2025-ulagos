# Se crea clase
class ReservaHostal:
    
    # Se crea los componentes de la clase
    def __init__(self, nombre_cliente, fecha_entrada, fecha_salida, num_habitacion):
        
        # Definiendo cada componente
        self.nombre_cliente = str(nombre_cliente)
        self.fecha_entrada = int(fecha_entrada)
        self.fecha_salida = int(fecha_salida)
        self.num_habitacion = int(num_habitacion)
    
    # Métodos
    
    # Un método para calcular la duración de la estadía del cliente
    def duracion_estadia_cliente(self):
        # Calculamos la diferencia entre fecha de salida y entrada
        # suponiendo que usamos el sistema de días del año
        duracion = self.fecha_salida - self.fecha_entrada
        return duracion
    
    # Método mágico para mostrar la información de la reserva
    def __str__(self):
        duracion = self.duracion_estadia_cliente()
        return f"""=== INFORMACIÓN DE LA RESERVA ===
Cliente: {self.nombre_cliente}
Habitación: {self.num_habitacion}
Fecha entrada (día del año): {self.fecha_entrada}
Fecha salida (día del año): {self.fecha_salida}
Duración de estadía: {duracion} días"""
    
    # Un método para cambiar la fecha de salida
    def cambiar_fecha_salida(self, nueva_fecha_salida):
        nueva_fecha_salida = int(nueva_fecha_salida)
        
        # Validar que la nueva fecha sea posterior a la entrada
        if nueva_fecha_salida <= self.fecha_entrada:
            print(f"ERROR: La fecha de salida ({nueva_fecha_salida}) debe ser posterior a la fecha de entrada ({self.fecha_entrada})")
            return False
        
        fecha_anterior = self.fecha_salida
        self.fecha_salida = nueva_fecha_salida
        
        print(f"Fecha de salida cambiada:")
        print(f"  Anterior: día {fecha_anterior}")
        print(f"  Nueva: día {self.fecha_salida}")
        print(f"  Nueva duración: {self.duracion_estadia_cliente()} días")
        return True
    
    # Método adicional para eliminar/cancelar reserva
    def cancelar_reserva(self):
        print(f"Cancelando reserva de {self.nombre_cliente} en habitación {self.num_habitacion}")
        print("Reserva cancelada exitosamente")
        # Marcamos los atributos como None para indicar cancelación
        self.nombre_cliente = "CANCELADO"
        self.fecha_entrada = 0
        self.fecha_salida = 0
        self.num_habitacion = 0


# Ejemplos de uso:
print("=== CREANDO RESERVAS ===")

# Crear reservas
reserva1 = ReservaHostal("Juan Pérez", 100, 107, 205)
reserva2 = ReservaHostal("María García", 150, 160, 301)
reserva3 = ReservaHostal("Carlos López", 200, 205, 102)

print("Reserva 1:")
print(reserva1)  # Usa el método mágico __str__

print("\nReserva 2:")
print(reserva2)

print("\nReserva 3:")
print(reserva3)

print("\n" + "="*50)
print("=== MODIFICANDO FECHAS ===")

# Cambiar fecha de salida de la reserva1
print(f"\nCambiando fecha de salida de {reserva1.nombre_cliente}:")
reserva1.cambiar_fecha_salida(110)  # Extender estadía
print("\nReserva actualizada:")
print(reserva1)

# Intentar cambiar a una fecha inválida
print(f"\nIntentando cambiar fecha de salida de {reserva2.nombre_cliente} a una fecha inválida:")
reserva2.cambiar_fecha_salida(140)  # Fecha anterior a la entrada (error)

print("\n" + "="*50)
print("=== ELIMINANDO/CANCELANDO RESERVA ===")

print(f"\nAntes de cancelar - Reserva 3:")
print(reserva3)

print(f"\nCancelando reserva de {reserva3.nombre_cliente}:")
reserva3.cancelar_reserva()

print(f"\nDespués de cancelar:")
print(reserva3)

print("\n" + "="*50)
print("=== ESTADÍSTICAS FINALES ===")

reservas_activas = [reserva1, reserva2]  # reserva3 fue cancelada
total_dias = sum(reserva.duracion_estadia_cliente() for reserva in reservas_activas)
print(f"Reservas activas: {len(reservas_activas)}")
print(f"Total días de reservas activas: {total_dias}")
print(f"Promedio días por reserva: {total_dias/len(reservas_activas):.1f}")

"""
no pude realizar el bendito ejercicio me equivocaba en cosas minimas y me pique pero ahora se 
"""