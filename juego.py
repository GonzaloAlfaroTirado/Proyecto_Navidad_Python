def descubrir(self, f, c):
        if self.esta_terminado or not self._coordenadas_validas(f, c):
            return

        if self.tablero_visible[f][c] != '■':
            print("No puedes descubrir una casilla marcada o ya revelada.")
            return
        
        valor = self.tablero_real.tablero[f][c]

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