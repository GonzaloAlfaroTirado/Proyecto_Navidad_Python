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

def verificar_hundimiento(tablero_visto, registro_barcos):
    for i, barco in enumerate(registro_barcos):
        # Si todas las coordenadas de este barco están marcadas como TOCADO ('X')
        if all(tablero_visto[f][c] == SIMBOLO_TOCADO for f, c in barco["coords"]):
            nombre = barco["nombre"]
            registro_barcos.pop(i) # Lo borramos para que no avise más veces
            return nombre
    return None

def hay_ganador(registro_barcos):
    return len(registro_barcos) == 0