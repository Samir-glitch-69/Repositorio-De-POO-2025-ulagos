class Persona():

    def __init__(self, nombre, apellido, edad,altura,peso):
        self.nombre = str(nombre)
        self.apellido = str(apellido)
        self.edad = int(edad)
        self.altura = float(altura)
        self.peso = float(peso) 

    def hablar(self):
        print(f"{self.nombre} esta hablando")
        
    def caminar(self):
        print(f"{self.nombre} esta caminando")
    
    def Calcular_Imc(self):
        imc = round(self.peso/(self.altura ** 2), 2)

        print(f"Calculo de IMC: {imc}, estas ")

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



persona1 = Persona("Cristina", "Torres", 23, 1.6, 63) 
persona2 = Persona("Benjamin", "Gomez", 20, 2.0, 90)


print(f"{persona1.nombre}")
print(f"{persona1.apellido}")
print(f"{persona1.edad}")
print(f"{persona1.altura}")
print(f"{persona1.peso}")

persona1.hablar()
persona2.caminar()
persona1.Calcular_Imc()

