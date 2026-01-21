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

    def _colocar_minas(self):
        # Coloca minas aleatoriamente sin repetir posiciones
        minas_colocadas = 0

        while minas_colocadas < self.minas:
            f = random.randint(0, self.filas - 1)
            c = random.randint(0, self.columnas - 1)

            if self.tablero[f][c] != -1:
                self.tablero[f][c] = -1
                minas_colocadas += 1
