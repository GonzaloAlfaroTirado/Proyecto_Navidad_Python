import random

class Tablero:
    def __init__(self, filas, columnas, minas):
        # Crea el tablero vacío y coloca minas
        self.filas = filas
        self.columnas = columnas
        self.minas = minas