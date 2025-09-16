import math
import matplotlib.pyplot as plt
import numpy as np

class FuncionTrigonometrica:
    """
    Clase para representar, graficar y evaluar funciones trigonométricas.
    
    Admite funciones de la forma: f(x) = amplitud * funcion((2π/periodo) * x)
    donde funcion puede ser seno, coseno o tangente.
    """
    
    TIPOS_VALIDOS = ['seno', 'coseno', 'tangente', 'sin', 'cos', 'tan']
    
    def __init__(self, tipo_funcion, amplitud=1, periodo=2*math.pi):
        """
        Inicializa una función trigonométrica.
        
        Args:
            tipo_funcion (str): Tipo de función ('seno', 'coseno', 'tangente')
            amplitud (float): Amplitud de la función (por defecto 1)
            periodo (float): Periodo de la función (por defecto 2π)
        """
        if tipo_funcion.lower() not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo de función inválido. Use: {self.TIPOS_VALIDOS[:3]}")
        
        # Normalizar el tipo de función
        tipo_normalizado = {
            'seno': 'seno', 'sin': 'seno',
            'coseno': 'coseno', 'cos': 'coseno',
            'tangente': 'tangente', 'tan': 'tangente'
        }
        
        self.tipo_funcion = tipo_normalizado[tipo_funcion.lower()]
        self.amplitud = amplitud
        self.periodo = periodo
        
        # Calcular la frecuencia angular (ω = 2π/T)
        self.frecuencia_angular = 2 * math.pi / periodo
    
    def evaluar(self, x):
        """
        Evalúa la función trigonométrica en un valor x (en radianes).
        
        Args:
            x (float): Valor en radianes donde evaluar la función
            
        Returns:
            float: Valor de la función en x
        """
        # Calcular el argumento: ω * x
        argumento = self.frecuencia_angular * x
        
        # Evaluar según el tipo de función
        if self.tipo_funcion == 'seno':
            return self.amplitud * math.sin(argumento)
        elif self.tipo_funcion == 'coseno':
            return self.amplitud * math.cos(argumento)
        elif self.tipo_funcion == 'tangente':
            return self.amplitud * math.tan(argumento)
    
    def graficar(self, x_min=-2*math.pi, x_max=2*math.pi, puntos=1000):
        """
        Grafica la función trigonométrica en un intervalo de valores.
        
        Args:
            x_min (float): Valor mínimo del intervalo (por defecto -2π)
            x_max (float): Valor máximo del intervalo (por defecto 2π)
            puntos (int): Número de puntos para la gráfica (por defecto 1000)
        """
        # Generar valores x
        x = np.linspace(x_min, x_max, puntos)
        
        # Calcular valores y
        y = []
        for xi in x:
            try:
                yi = self.evaluar(xi)
                # Limitar valores extremos para tangente
                if self.tipo_funcion == 'tangente' and abs(yi) > 10:
                    yi = np.nan
                y.append(yi)
            except:
                y.append(np.nan)
        
        y = np.array(y)
        
        # Crear la gráfica
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'b-', linewidth=2, label=str(self))
        plt.grid(True, alpha=0.3)
        plt.xlabel('x (radianes)')
        plt.ylabel('f(x)')
        plt.title(f'Gráfica de {str(self)}')
        plt.legend()
        
        # Agregar líneas de referencia
        plt.axhline(y=0, color='k', linewidth=0.5)
        plt.axvline(x=0, color='k', linewidth=0.5)
        
        # Configurar límites del eje y
        if self.tipo_funcion != 'tangente':
            plt.ylim(-abs(self.amplitud) * 1.2, abs(self.amplitud) * 1.2)
        else:
            plt.ylim(-10, 10)
        
        plt.show()
    
    def __str__(self):
        """
        Método mágico que devuelve una representación de texto de la función.
        
        Returns:
            str: Representación matemática de la función
        """
        # Determinar el símbolo de la función
        simbolos = {
            'seno': 'sin',
            'coseno': 'cos',
            'tangente': 'tan'
        }
        simbolo = simbolos[self.tipo_funcion]
        
        # Construir la representación
        if self.amplitud == 1:
            amplitud_str = ""
        elif self.amplitud == -1:
            amplitud_str = "-"
        else:
            amplitud_str = f"{self.amplitud}"
        
        # Calcular el coeficiente de x
        if self.frecuencia_angular == 1:
            coef_str = "x"
        elif abs(self.frecuencia_angular - 2*math.pi) < 1e-10:
            coef_str = "2πx"
        elif abs(self.frecuencia_angular - math.pi) < 1e-10:
            coef_str = "πx"
        else:
            coef_str = f"{self.frecuencia_angular:.3f}x"
        
        return f"f(x) = {amplitud_str}{simbolo}({coef_str})"
    
    def __repr__(self):
        """Representación técnica de la función."""
        return f"FuncionTrigonometrica(tipo='{self.tipo_funcion}', amplitud={self.amplitud}, periodo={self.periodo})"
    
    def valores_criticos(self, num_periodos=2):
        """
        Devuelve los valores críticos de la función (máximos, mínimos y ceros).
        
        Args:
            num_periodos (int): Número de periodos a considerar (por defecto 2)
            
        Returns:
            dict: Diccionario con los valores críticos
        """
        criticos = {
            'maximos': [],
            'minimos': [],
            'ceros': []
        }
        
        # Generar puntos en el intervalo especificado
        x_max = num_periodos * self.periodo
        
        if self.tipo_funcion == 'seno':
            # Para seno: máximos en π/2 + 2πk, mínimos en 3π/2 + 2πk, ceros en πk
            for k in range(-num_periodos, num_periodos + 1):
                # Máximos
                x_max_val = (math.pi/2 + 2*math.pi*k) / self.frecuencia_angular
                if abs(x_max_val) <= x_max:
                    criticos['maximos'].append((x_max_val, self.amplitud))
                
                # Mínimos
                x_min_val = (3*math.pi/2 + 2*math.pi*k) / self.frecuencia_angular
                if abs(x_min_val) <= x_max:
                    criticos['minimos'].append((x_min_val, -self.amplitud))
                
                # Ceros
                x_cero = (math.pi*k) / self.frecuencia_angular
                if abs(x_cero) <= x_max:
                    criticos['ceros'].append((x_cero, 0))
        
        elif self.tipo_funcion == 'coseno':
            # Para coseno: máximos en 2πk, mínimos en π + 2πk, ceros en π/2 + πk
            for k in range(-num_periodos, num_periodos + 1):
                # Máximos
                x_max_val = (2*math.pi*k) / self.frecuencia_angular
                if abs(x_max_val) <= x_max:
                    criticos['maximos'].append((x_max_val, self.amplitud))
                
                # Mínimos
                x_min_val = (math.pi + 2*math.pi*k) / self.frecuencia_angular
                if abs(x_min_val) <= x_max:
                    criticos['minimos'].append((x_min_val, -self.amplitud))
                
                # Ceros
                x_cero = (math.pi/2 + math.pi*k) / self.frecuencia_angular
                if abs(x_cero) <= x_max:
                    criticos['ceros'].append((x_cero, 0))
        
        elif self.tipo_funcion == 'tangente':
            # Para tangente: no hay máximos/mínimos globales, solo ceros y asíntotas
            for k in range(-num_periodos*2, num_periodos*2 + 1):
                # Ceros
                x_cero = (math.pi*k) / self.frecuencia_angular
                if abs(x_cero) <= x_max:
                    criticos['ceros'].append((x_cero, 0))
            
            # Asíntotas verticales
            criticos['asintotas'] = []
            for k in range(-num_periodos*2, num_periodos*2 + 1):
                x_asintota = (math.pi/2 + math.pi*k) / self.frecuencia_angular
                if abs(x_asintota) <= x_max:
                    criticos['asintotas'].append(x_asintota)
        
        # Ordenar los valores críticos
        for key in criticos:
            if key != 'asintotas':
                criticos[key].sort()
            else:
                criticos[key].sort()
        
        return criticos
    
    def informacion_completa(self):
        """
        Devuelve información completa sobre la función.
        
        Returns:
            str: Información detallada de la función
        """
        info = f"""
=== INFORMACIÓN DE LA FUNCIÓN TRIGONOMÉTRICA ===
Función: {str(self)}
Tipo: {self.tipo_funcion}
Amplitud: {self.amplitud}
Periodo: {self.periodo:.4f}
Frecuencia angular (ω): {self.frecuencia_angular:.4f}

Propiedades:
- Dominio: {"ℝ - {π/2 + πk | k ∈ ℤ}" if self.tipo_funcion == 'tangente' else "ℝ (todos los reales)"}
- Rango: {"ℝ (todos los reales)" if self.tipo_funcion == 'tangente' else f"[{-abs(self.amplitud)}, {abs(self.amplitud)}]"}
- Es par: {'Sí' if self.tipo_funcion == 'coseno' else 'No'}
- Es impar: {'Sí' if self.tipo_funcion in ['seno', 'tangente'] else 'No'}
"""
        return info


# Ejemplo de uso y pruebas
if __name__ == "__main__":
    print("=== EJEMPLOS DE USO DE LA CLASE FuncionTrigonometrica ===\n")
    
    # Crear diferentes funciones trigonométricas
    f1 = FuncionTrigonometrica('seno', amplitud=2, periodo=math.pi)
    f2 = FuncionTrigonometrica('coseno', amplitud=1.5)
    f3 = FuncionTrigonometrica('tangente', amplitud=1, periodo=math.pi)
    
    # Mostrar representación de las funciones
    print("1. REPRESENTACIÓN DE FUNCIONES:")
    print(f"f1: {f1}")
    print(f"f2: {f2}")
    print(f"f3: {f3}")
    print()
    
    # Evaluar funciones en diferentes puntos
    print("2. EVALUACIÓN EN DIFERENTES PUNTOS:")
    puntos_prueba = [0, math.pi/4, math.pi/2, math.pi]
    
    for punto in puntos_prueba:
        print(f"En x = {punto:.4f}:")
        print(f"  f1({punto:.4f}) = {f1.evaluar(punto):.4f}")
        print(f"  f2({punto:.4f}) = {f2.evaluar(punto):.4f}")
        if punto != math.pi/2:  # Evitar división por cero en tangente
            print(f"  f3({punto:.4f}) = {f3.evaluar(punto):.4f}")
        print()
    
    # Mostrar valores críticos
    print("3. VALORES CRÍTICOS:")
    for i, func in enumerate([f1, f2, f3], 1):
        print(f"\nFunción f{i}: {func}")
        criticos = func.valores_criticos(num_periodos=1)
        for tipo, valores in criticos.items():
            if valores:
                print(f"  {tipo.capitalize()}: {valores}")
    
    # Mostrar información completa
    print("\n4. INFORMACIÓN COMPLETA DE f1:")
    print(f1.informacion_completa())
    
    # Graficar las funciones y triángulos (descomenta para mostrar gráficas)
    print("5. GRÁFICAS (descomenta las siguientes líneas para mostrar):")
    print("# f1.graficar()")
    print("# f2.graficar()")
    print("# f3.graficar(x_min=-2*math.pi, x_max=2*math.pi)")
    
    print("\n6. GRÁFICAS DE TRIÁNGULOS:")
    print("# f1.graficar_triangulo_unitario(math.pi/3)")
    print("# f1.graficar_triangulo_rectangular(3, 4)")
    print("# f1.graficar_funcion_con_triangulo(math.pi/4)")
    print("# f1.comparar_triangulos_multiples([math.pi/6, math.pi/4, math.pi/3, math.pi/2])")
    
    # Ejemplo de triángulo rectangular
    print("\n7. EJEMPLO DE TRIÁNGULO RECTANGULAR:")
    resultado = f1.graficar_triangulo_rectangular(5, 12, mostrar_calculos=False)
    print("Resultado del triángulo 5-12:")
    for clave, valor in resultado.items():
        print(f"  {clave}: {valor}")
    
    # Ejemplo práctico con ángulos comunes
    print("\n8. ÁNGULOS COMUNES EN RADIANES:")
    angulos_comunes = {
        "30°": math.pi/6,
        "45°": math.pi/4, 
        "60°": math.pi/3,
        "90°": math.pi/2
    }
    
    for grado, radian in angulos_comunes.items():
        print(f"{grado} = {radian:.4f} rad")
        print(f"  sen({grado}) = {math.sin(radian):.4f}")
        print(f"  cos({grado}) = {math.cos(radian):.4f}")
        if radian != math.pi/2:
            print(f"  tan({grado}) = {math.tan(radian):.4f}")
        print()