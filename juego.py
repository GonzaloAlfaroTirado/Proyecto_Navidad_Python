def verificar_hundimiento(tablero_visto, registro_barcos):
    for i, barco in enumerate(registro_barcos):
        # Si todas las coordenadas de este barco están marcadas como TOCADO ('X')
        if all(tablero_visto[f][c] == SIMBOLO_TOCADO for f, c in barco["coords"]):
            nombre = barco["nombre"]
            registro_barcos.pop(i) # Lo borramos para que no nos avise más veces
            return nombre
    return None
