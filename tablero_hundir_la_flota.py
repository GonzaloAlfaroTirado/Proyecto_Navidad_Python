import random

SIMBOLO_AGUA = "~"
SIMBOLO_BARCO = "B"
SIMBOLO_TOCADO = "X"
SIMBOLO_FALLO = "O"

def crear_tablero(tamano):
    return [[SIMBOLO_AGUA for _ in range(tamano)] for _ in range(tamano)]

def mostrar_tableros_paralelos(tab_jugador, tab_disparos):
    tam = len(tab_jugador)
    header = "    " + " ".join([str(i).ljust(2) for i in range(tam)])
    print("\n" + header + "          " + header)
    print("  " + "—" * (tam * 3) + "        " + "—" * (tam * 3))
    
    for i in range(tam):
        letra = chr(65 + i)
        fila_j = "  ".join(tab_jugador[i])
        fila_d = "  ".join(tab_disparos[i])
        print(f"{letra} | {fila_j}      {letra} | {fila_d}")
    print("\n   TU FLOTA (Izquierda)      |      TUS DISPAROS (Derecha)")
def es_posicion_valida(tablero, fila, col, longitud, orientacion):
    tam = len(tablero)
    for i in range(longitud):
        r, c = (fila + i, col) if orientacion == "V" else (fila, col + i)
        
        if not (0 <= r < tam and 0 <= c < tam):
            return False
        
        # Regla: No tocar otros barcos (revisar 3x3 alrededor de cada celda)
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                nr, nc = r + dr, c + dc
                if 0 <= nr < tam and 0 <= nc < tam:
                    if tablero[nr][nc] == SIMBOLO_BARCO:
                        return False
    return True