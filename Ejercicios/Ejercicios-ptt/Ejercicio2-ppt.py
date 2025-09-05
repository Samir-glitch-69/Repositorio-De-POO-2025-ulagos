
class Coche:
    def __init__(self, marca, gasolina):
        """
        Inicializa un objeto Coche.
        
        Args:
            marca (str): La marca del coche
            gasolina (float): La cantidad inicial de gasolina en litros
        """
        #le faltaba colocar el str y el float, el kmetros receorrido ya estaba definido como un float
        self.marca = str(marca)
        self.gasolina = float(gasolina)
        self.kilometros_recorridos = 0.0
    
    def conducir(self, kilometros):
        """
        Conduce el coche una determinada distancia.
        Consume 1 litro de gasolina por cada 10 kilómetros.
        
        Args:
            kilometros (float): Kilómetros a recorrer
        """
        #por bucle zerodivision
        if kilometros <= 0:
            print("La distancia debe ser mayor a 0 kilómetros.")
            return
        
        # Calcular gasolina necesaria (1 litro por cada 10 km)
        gasolina_necesaria = kilometros / 10
        
        if self.gasolina >= gasolina_necesaria:
            # Hay suficiente gasolina para el viaje completo
            self.kilometros_recorridos += kilometros
            self.gasolina -= gasolina_necesaria
            # se coloca el .2f para abreviar los decimales
            print(f"Has conducido {kilometros} km. Gasolina restante: {self.gasolina:.2f} litros.")
        else:
            # No hay suficiente gasolina, conducir solo hasta donde alcance
            kilometros_posibles = self.gasolina * 10
            self.kilometros_recorridos += kilometros_posibles
            self.gasolina = 0
            print(f"¡Te has quedado sin gasolina! Solo pudiste recorrer {kilometros_posibles:.2f} km de los {kilometros} km solicitados.")
    
    def cargar_gasolina(self, litros):
        """
        Carga gasolina al coche.
        
        Args:
            litros (float): Litros de gasolina a agregar
        """
        if litros <= 0:
            print("La cantidad de gasolina debe ser mayor a 0 litros.")
            return
        
        self.gasolina += litros
        print(f"Has cargado {litros} litros de gasolina. Gasolina total: {self.gasolina:.2f} litros.")
    
    def mostrar_estado(self):
        """
        Muestra el estado actual del coche.
        """
        print(f"\n--- Estado del {self.marca} ---")
        print(f"Gasolina: {self.gasolina:.2f} litros")
        print(f"Kilómetros recorridos: {self.kilometros_recorridos:.2f} km")
        print("----------------------------\n")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un coche
    mi_coche = Coche("Toyota", 15.0)
    
    # Mostrar estado inicial
    mi_coche.mostrar_estado()
    
    # Conducir 50 km (necesita 5 litros)
    mi_coche.conducir(50)
    
    # Conducir 80 km (necesita 8 litros)
    mi_coche.conducir(80)
    
    # Intentar conducir 100 km (necesitaría 10 litros, pero solo quedan 2)
    mi_coche.conducir(100)
    
    # Cargar gasolina
    mi_coche.cargar_gasolina(20)
    
    # Conducir nuevamente
    mi_coche.conducir(50)
    
    # Mostrar estado final
    mi_coche.mostrar_estado()

    """
    colocar el objetivo de cada def debajo para dar conteexto
    colocar los argumentos de cada uno de los def debajo para poder ver los errores

    """