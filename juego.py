from tablero_hundir_la_flota import SIMBOLO_BARCO, SIMBOLO_TOCADO, SIMBOLO_AGUA, SIMBOLO_FALLO

def procesar_disparo(tablero_oculto, tablero_visto, fila, col):
    if not (0 <= fila < len(tablero_oculto) and 0 <= col < len(tablero_oculto)):
        return "FUERA"
    
    if tablero_visto[fila][col] in [SIMBOLO_TOCADO, SIMBOLO_FALLO]:
        return "REPETIDO"
    
    if tablero_oculto[fila][col] == SIMBOLO_BARCO:
        tablero_oculto[fila][col] = SIMBOLO_TOCADO
        tablero_visto[fila][col] = SIMBOLO_TOCADO
        return "TOCADO"
    else:
        tablero_visto[fila][col] = SIMBOLO_FALLO
        return "AGUA"
