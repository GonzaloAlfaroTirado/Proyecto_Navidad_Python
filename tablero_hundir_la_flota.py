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