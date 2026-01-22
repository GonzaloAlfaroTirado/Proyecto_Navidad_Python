"""Buscaminas"""

from tablero import Tablero

class Juego:
    def __init__(self, filas=8, columnas=8, minas=10):
        self.filas = filas
        self.columnas = columnas
        self.minas = minas

        self.tablero_real = Tablero(filas, columnas, minas)
        self.tablero_visible = [['■' for _ in range(columnas)] for _ in range(filas)]

        self.esta_terminado = False
        self.gano = False

        self.casillas_sin_mina = filas * columnas - minas
        self.casillas_descubiertas = 0
        self.primer_movimiento = True
        self.simbolo_mina = 'X'
        self.banderas = 0

    def _coordenadas_validas(self, f, c):
        return 0 <= f < self.filas and 0 <= c < self.columnas
    
    #Primer commit del buscaminas