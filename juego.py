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
    
    def descubrir(self, f, c):
        if self.esta_terminado or not self._coordenadas_validas(f, c):
            return

        if self.tablero_visible[f][c] != '■':
            print("No puedes descubrir una casilla marcada o ya revelada.")
            return
        
        valor = self.tablero_real.tablero[f][c]

        # Lógica de primer movimiento (se completará en el siguiente commit)
        if self.primer_movimiento and valor == -1:
            self._recolocar_minas_alejadas_de(f, c)
            valor = self.tablero_real.tablero[f][c]

        self.primer_movimiento = False

        if valor == -1:
            self.tablero_visible[f][c] = self.simbolo_mina
            print(f"\n{self.simbolo_mina} ¡HAS PISADO UNA MINA! {self.simbolo_mina}")
            self.esta_terminado = True
            self.gano = False
            return

        self._revelar_casilla(f, c, valor)

        if self.casillas_descubiertas == self.casillas_sin_mina:
            self.esta_terminado = True
            self.gano = True

    def _revelar_casilla(self, f, c, valor):
        self.tablero_visible[f][c] = str(valor) if valor > 0 else ' '
        self.casillas_descubiertas += 1
        
        if valor == 0:
            self._propagar_ceros(f, c)
            
    
    
    def _propagar_ceros(self, f, c):
        direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for df, dc in direcciones:
            nf, nc = f + df, c + dc
            if self._coordenadas_validas(nf, nc) and self.tablero_visible[nf][nc] == '■':
                valor = self.tablero_real.tablero[nf][nc]
                self.tablero_visible[nf][nc] = str(valor) if valor > 0 else ' '
                self.casillas_descubiertas += 1
                if valor == 0:
                    self._propagar_ceros(nf, nc)

    def _recolocar_minas_alejadas_de(self, f, c):
        from random import sample
        posiciones = [(i, j) for i in range(self.filas) for j in range(self.columnas) if not (i == f and j == c)]
        nuevas_minas = set(sample(posiciones, self.minas))

        self.tablero_real.tablero = [[0 for _ in range(self.columnas)] for _ in range(self.filas)]
        for (i, j) in nuevas_minas:
            self.tablero_real.tablero[i][j] = -1
        self.tablero_real._calcular_numeros()
        
        #Tercer commit buscaminas
    def marcar(self, f, c):
        if self.esta_terminado or not self._coordenadas_validas(f, c):
            return

        actual = self.tablero_visible[f][c]
        if actual == '■':
            self.tablero_visible[f][c] = 'F'
            self.banderas += 1
        elif actual == 'F':
            self.tablero_visible[f][c] = '■'
            self.banderas -= 1
        
        self._comprobar_victoria_por_banderas()

    def _comprobar_victoria_por_banderas(self):
        if self.banderas != self.minas:
            return

        for f in range(self.filas):
            for c in range(self.columnas):
                if self.tablero_visible[f][c] == 'F' and self.tablero_real.tablero[f][c] != -1:
                    return 

        self.esta_terminado = True
        self.gano = True
        print("\n ¡VICTORIA! ¡HAS MARCADO TODAS LAS MINAS CORRECTAMENTE!")