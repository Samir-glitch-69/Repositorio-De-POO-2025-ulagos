#se crea la clase
class Persona():
    
#se define que tiene la clase, se comienza con un innit
    def __init__(self, nombre, apellido, edad, altura, peso, nota1, nota2, nota3):
        self.nombre = str(nombre)
        self.apellido = str(apellido)
        self.edad = int(edad)
        self.altura = float(altura)
        self.peso = float(peso)
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)
        self.nota3 = float(nota3)

# se crea la funcion hablar
    def hablar(self):
        print(f"{self.nombre} esta hablando")
        
#se crea la funcion caminar
    def caminar(self):
        print(f"{self.nombre} esta caminando")

# se crea la funcion calcular imc
    def Calcular_Imc(self):

#formula deel imc
        imc = round(self.peso/(self.altura ** 2), 2)

        print(f"Calculo de IMC: {imc}")

        if imc < 18.5:
            print(f"su imc es: {imc}, estas Bajo peso")
        elif 18.5 <= imc < 24.9:
            print(f"su imc es: {imc}, estas Peso normal")
        elif 25 <= imc < 29.9:
            print(f"su imc es: {imc}, estas Sobrepeso")
        elif 30 <= imc < 34.9:
            print(f"su imc es: {imc}, estas Obesidad grado I")
        elif 35 <= imc < 39.9:
            print(f"su imc es: {imc}, estas Obesidad grado II")
        else:
            print(f"su imc es: {imc}, estas Obesidad grado III")

#se creae ele promedio de asignaturas
    def Promedio_asignatura(self):

        promedio = (self.nota1 + self.nota2 + self.nota3) / 3
        promedio = round(promedio, 2)

        print(f"notas de {self.nombre}: {self.nota1}, {self.nota2}, {self.nota3}")
        print(f"promedio: {promedio}")
        if promedio >= 4.0:
            print(f"{self.nombre} aprobo la asignatura con promedio {promedio}")
        else:
            print(f"{self.nombre} no aprobo la asignatura con promedio {promedio}")



#se crean los objetos personas
persona1 = Persona("Cristina", "Torres", 23, 1.6, 63, 4.0, 4.9, 5.0) 
persona2 = Persona("Benjamin", "Gomez", 20, 2.0, 90, 3.0, 2.0, 4.5)


print(f"{persona1.nombre}")
print(f"{persona1.apellido}")
print(f"{persona1.edad}")
print(f"{persona1.altura}")
print(f"{persona1.peso}")

persona1.hablar()
persona2.caminar()
persona1.Calcular_Imc()
persona1.Promedio_asignatura()

