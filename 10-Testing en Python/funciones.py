# Módulo de funciones matemáticas

def calcula_media(*args):
    # args llega como una tupla que contiene la lista: ([10, 10, 10],).
    # Por eso se desempaqueta con sum(*args) y len(*args).
    return sum(*args) / len(*args)