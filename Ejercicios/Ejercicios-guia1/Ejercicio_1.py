#se crea clase
class ReservaHostal():

#se crea los componentes de la clase
    def __init__(self, Nombre_cliente, dia_entrada, mes_entrada, dia_salida, mes_salida, num_habitacion):

#definiendo cada componente
        Nombre_cliente = str(Nombre_cliente)

        dia_entrada = int(dia_entrada)
        mes_salida = int(mes_salida)

        dia_salida = int(dia_salida)
        mes_entrada = int(mes_entrada)
        
        num_habitacion = int(num_habitacion)

#Metodos

#Un método para calcular la duración de la estadía del cliente.

#suponiendo que no tenemos el datetime ni ningun tipo de importacion se va a usar un formato de 365 dias 

#suponiendo que el dia 5 de septiembre es el 05-09-2025 entonces hacemos un promedio de 9 x 30 y los 5 dias


