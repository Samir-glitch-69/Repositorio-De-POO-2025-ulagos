class FuncionTrigonometrica:
    """
● Atributos:
○ Tipo de función (seno, coseno, tangente)
○ Amplitud y periodo de la función.

    """

    def __init__(self, seno, coseno, tangente, amplitud, periodo_funcion):
        seno = float(seno)
        coseno = float(coseno)
        tangente = float(tangente)
        amplitud = float(amplitud)
        periodo_funcion =float(periodo_funcion)

#● Métodos:

#○ Crear un método que evalúe la función trigonométrica en un valor x (enradianes)