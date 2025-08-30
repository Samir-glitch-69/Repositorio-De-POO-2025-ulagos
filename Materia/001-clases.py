# GUIA RÁPIDA DE CLASES EN PYTHON
# Docente: Victor Saldivia Vera - Institución: Universidad de Los Lagos

# Nota estudiante las clases siempre van con mayuscula al principio 
# Nota estudiante dentro de la clase todo va con sangría 
# Nota estudiante El self es una referencia a si mismo cuando se crea un objeto podiendo acceder 
# a la diferente informacion de la clase 
# el constructor innit siempre va 
# de la clase automovil se van a compartir los atributos que esten adentro de este 
class Persona():
    
    # Constructor de Clase
    def __init__(self, nombre, apellido, edad): # este método se ejecuta automáticamente al crear un nuevo objeto
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    # Atributos (Características compartidas por todos los objetos de la clase)
    # nombre = "Cristina"
    # apellido = "Torres"
    # edad = 23
    
    # Métodos (Comportamientos)
    
    def hablar(self):
        print(f"{self.nombre} esta hablando")
        
    def caminar(self):
        print(f"{self.nombre} esta caminando")
        
        
persona1 = Persona("Cristina", "Torres", 23) # instancia de la clase Persona -> crear un objeto de la clase Persona
persona2 = Persona("Benjamin", "Gomez", 20)


print(f"{persona1.nombre}")
print(f"{persona1.apellido}")
print(f"{persona1.edad}")

persona1.hablar() # equivalente a Persona.hablar(persona1)
persona2.caminar() # se puede crear múltiples objetos de la misma clase
        
        