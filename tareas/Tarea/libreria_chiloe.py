class Libreria:
    __descuento_socios = 0.05  

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__catalogo = {}
        self.__carrito = []
        self.__compras_realizadas = 0

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_catalogo(self):
        return self.__catalogo

    @classmethod
    def get_descuento(cls):
        return cls.__descuento_socios

    @classmethod
    def set_descuento(cls, nuevo_descuento):
        if 0.05 <= nuevo_descuento <= 0.10:
            cls.__descuento_socios = nuevo_descuento
        else:
            raise ValueError("El descuento tiene qe estar entre 0.05 y 0.10")

    def agregar_libro_catalogo(self, titulo, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self.__catalogo[titulo] = precio

    def mostrar_catalogo(self):
        print("\n==============================")
        print("catalogo de libros".center(30, "-"))
        print("==============================")
        if not self.__catalogo:
            print("El catalogo esta vacio")
        else:
            for titulo, precio in self.__catalogo.items():
                print(f"{titulo} - ${precio}")
                print("------------------------------")

    def agregar_al_carrito(self, titulo: str):
        titulo_normalizado = titulo.strip().lower()
        titulos_catalogo = {t.lower(): t for t in self.__catalogo.keys()}  

        if titulo_normalizado in titulos_catalogo:
            self.__carrito.append(titulos_catalogo[titulo_normalizado])
        else:
            raise AssertionError("El libro no existe dentro del catalogo")

    def calcular_total(self, frecuente=False):
        if not self.__carrito:
            print("El carrito esta vacio")
            return 0
        total = sum(self.__catalogo[titulo] for titulo in self.__carrito)

        if frecuente:
            total = Libreria.aplicar_descuento(total, Libreria.get_descuento())
        return total

    def finalizar_compra(self):
        self.__compras_realizadas += 1
        self.__carrito = []

    def get_compras_realizadas(self):
        return self.__compras_realizadas

    @staticmethod
    def aplicar_descuento(monto, descuento):
        if monto < 0:
            raise ValueError("El monto tiene que sert mayor a 0")
        if not 0.05 <= descuento <= 0.10:
            raise ValueError("El descuento debe estar en el rango de 0.05 a 0.10")
        return monto * (1 - descuento)

def cargar_libros_desde_txt(nombre_archivo):
    catalogo = {}
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(",")
                if len(partes) == 2:
                    titulo, precio = partes
                    try:
                        catalogo[titulo.strip()] = float(precio.strip())
                    except ValueError:
                        print(f"Precio invalido en la linea: {linea}")
                else:
                    print(f"Linea mal formada: {linea}")
    except FileNotFoundError:
        print(f"No se encontro el archivo: {nombre_archivo}")
    return catalogo

def cargar_socios(nombre_archivo):
    socios = {}
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(",")
                if len(partes) == 2:
                    nombre, compras = partes
                    try:
                        socios[nombre.strip()] = int(compras.strip())
                    except ValueError:
                        print(f"Compras invalidas en la linea: {linea}")
                else:
                    print(f"Linea mal formada: {linea}")
    except FileNotFoundError:
        print(f"No se encontro el archivo: {nombre_archivo}")
    return socios

def guardar_socios(nombre_archivo, socios):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for nombre, compras in socios.items():
            f.write(f"{nombre},{compras}\n")

if __name__ == "__main__":
    libreria = Libreria("Libreria chiloe")

    libros = cargar_libros_desde_txt("libros.txt")
    for titulo, precio in libros.items():
        libreria.agregar_libro_catalogo(titulo, precio)

    socios = cargar_socios("socios.txt")

    nombre_cliente = input("Ingresa tu nombre: ").strip()
    if nombre_cliente not in socios:
        socios[nombre_cliente] = 0

    while True:
        print("\n--- Opciones ---")
        print("1. Ver catalogo")
        print("2. Agregar libro al carrito")
        print("3. Total a pagar")
        print("4. Salir")
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            libreria.mostrar_catalogo()

        elif opcion == "2":
            titulo = input("Ingrese el titulo del libro: ")
            try:
                libreria.agregar_al_carrito(titulo)
                print(f"{titulo} fue agregado al carrito")
            except AssertionError as e:
                print("Error:", e)

        elif opcion == "3":
            compras_cliente = socios[nombre_cliente]
            frecuente = compras_cliente >= 3
            total = libreria.calcular_total(frecuente)
            if total == 0:
                print("No hay libros en el carrito.")
            else:
                if frecuente:
                    print(f"Total con el descuento de la libreria aplicado: ${total}")
                else:
                    print(f"Total a pagar (sin descuento): ${total}")
                    print(f"Llevas {compras_cliente} compras, con una cuarta compra obtienes un descuento")
                libreria.finalizar_compra()
                socios[nombre_cliente] += 1
                guardar_socios("socios.txt", socios)

        elif opcion == "4":
            print()
            print("Gracia por visitar Libreria Chiloe")
            break

        else:
            print("Opcion invalida, intenta de nuevo.")
