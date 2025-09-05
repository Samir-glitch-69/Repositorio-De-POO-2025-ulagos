# ejrcicio hecho por profesor en clase 

class Fraccion:
    def __init__(self, numerador, denominador=1):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        self.numerador = numerador
        self.denominador = denominador
    
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    
    def __add__(self, other):
        nuevo_denominador = self.denominador * other.denominador
        nuevo_numerador = (self.numerador * other.denominador + 
                          other.numerador * self.denominador)
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __mul__(self, other):
        nuevo_numerador = self.numerador * other.numerador
        nuevo_denominador = self.denominador * other.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __eq__(self, other):
        return (self.numerador * other.denominador == 
                self.denominador * other.numerador)

# Crear instancias para probar
fraccion1 = Fraccion(1, 2)
fraccion2 = Fraccion(3, 4)
fraccion3 = Fraccion(2, 4)

# Probar métodos
suma = fraccion1 + fraccion2
multiplicacion = fraccion1 * fraccion2
igualdad1 = fraccion1 == fraccion3
igualdad2 = fraccion1 == fraccion2

# Mostrar resultados
print("Fracción 1:", fraccion1)
print("Fracción 2:", fraccion2)
print("Fracción 3:", fraccion3)
print("Suma (1 + 2):", suma)
print("Multiplicación (1 * 2):", multiplicacion)
print("¿1 es igual a 3?", igualdad1)
print("¿1 es igual a 2?", igualdad2)