import numpy as np

def saludar():
    print("Hola, te saludo desde saludos.saludar()")

def prueba():
    print("Esto es una nueva prueba de la nueva versión 6.0")

def generar_array(numeros):
    return np.arange(numeros)

class Saludo:
    def __init__(self):
        print("Hola, te saludo desde saludo.__init__()")

# Hace que esta parte de código solo se ejecute si ejecutas directamente saludos.py
if __name__ == '__main__':
    saludar()