import random

class Tablero:
    def __init__(self, filas, columnas, minas):
        # Crea el tablero vacío y coloca minas
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        
        self.tablero = [[0 for _ in range(columnas)] for _ in range(filas)]

        self._colocar_minas()
        self._calcular_numeros()