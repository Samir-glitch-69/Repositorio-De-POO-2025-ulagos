class Cancion:
    #Ejemplo hecho por profesor del ultimo ejercicio mas dificil de la guia de estudio
    
    # Constructor de Clase
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = int(duracion_segundos) # que muestre los segundos como entero :)

    # Método de clase que Convierte de minutos a segundos
    def min_seg(self):
        # Convierte la duración total de la canción en formato mm:ss
        m, s = divmod(max(self.duracion_segundos, 0), 60) # divmod divide y obtiene el resto (en formato de tupla)
        return f"{m}:{s:02d}" # Ejemplo: 185 segundos -> "3:05"
    
    # Método mágico que muestra la canción utilizando un print()
    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.min_seg()})"


class Playlist:
    # Constructor de Clase
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = [] # Aqui se guardan las canciones (objetos de la clase Cancion)

     # Método de clase que agrega una canción a la lista de la playlist
    def agregar(self, cancion):
        self.canciones.append(cancion)

    # Método de clase que calcula la duración total de una Playlist
    def duracion_total(self):
        # Calcula la duración total de la playlist en segundos
        return sum(elemento.duracion_segundos for elemento in self.canciones)
    
    # Método de clase que convierte segundos al formato minutos:segundos (mm:ss)
    def min_seg_total(self):
        # Convierte la duración total de la playlist en formato mm:ss
        total = self.duracion_total()
        m, s = divmod(max(total, 0), 60)
        return f"{m}:{s:02d}"
    
    # Método mágico que devuelve la cantidad de canciones en la playlist
    def __len__(self):
        return len(self.canciones)

    # Método mágico que combina dos playlists en una nueva_playlist playlist
    def __add__(self, otra):
        nueva_playlist = Playlist(f"{self.nombre} + {otra.nombre}")  # Nombre de la nueva_playlist playlist
        nueva_playlist.canciones = self.canciones + otra.canciones  # Une las listas de canciones
        return nueva_playlist
        
    # Método mágico que devuelve el formato solicitado de la playlist
    def __str__(self):
        encabezado_playlist = f"Playlist: {self.nombre} | {len(self)} canciones | Total: {self.min_seg_total()}"
        if not self.canciones: # Si no tiene canciones la playlist
            return encabezado_playlist + "\n  (vacía)"
        lineas = [encabezado_playlist]
        for i, c in enumerate(self.canciones, start=1):  # Recorre las canciones numerándolas desde 1 en lugar de 0 (propiedad start)
            lineas.append(f"  {i}. {c}")
        return "\n".join(lineas) # Une todas los strings de la lista en un solo texto, adempas de separadas por saltos de línea ("\n")

# Ejemplo de uso (creación de objetos)

# Crear canciones (duración en segundos)
cancion1 = Cancion("The Real Slim Shady", "Eminem", 284)  # 284 seg = 4:44
cancion2 = Cancion("Not Like Us", "Kendrick Lamar", 274)
cancion3 = Cancion("Houdini", "Eminem", 227)
cancion4 = Cancion("Black Summer", "Red Hot Chili Peppers", 232)

# Crear playlist de Hip Hop y agregar canciones
playlist1 = Playlist("Hip Hop")
playlist1.agregar(cancion1)
playlist1.agregar(cancion2)
playlist1.agregar(cancion3)

# Crear playlist de Rock y agregar canción
playlist2 = Playlist("Rockcito")
playlist2.agregar(cancion4)

# Mostrar ambas playlists - con salto de lineas al final para que sea mas bonito :) 
print(playlist1)
print("\n")
print(playlist2)
print("\n")

# Combinar playlists con el operador + (__add__)
playlist3 = playlist1 + playlist2
print("Playlist Combinada:\n", playlist3) 

# Mostrar cantidad de canciones de la playlist combinada
print("\nCantidad de canciones en Playlist Combinada:", len(playlist3))