def jugar_partida(filas, columnas, minas):
    juego = Juego(filas=filas, columnas=columnas, minas=minas)

    print("\n=== BUSCAMINAS ===")
    print(f"Tablero: {filas}x{columnas} | Minas: {minas}")
    print("Introduce coordenadas como: fila columna (ej: 2 3)")
    print("Escribe 'salir' para terminar la partida.\n")

    while not juego.esta_terminado:
        print(f"\nBanderas colocadas: {juego.banderas}/{juego.minas}")
        for fila in juego.tablero_visible:
            print(" ".join(fila))

        entrada = input("\nSelecciona una casilla o escribe 'marcar f c': ").strip().lower()

        if entrada == "salir":
            print("\nHas decidido terminar la partida.")
            return
        if entrada.startswith("marcar"):
            try:
                _, f, c = entrada.split()
                f, c = int(f) - 1, int(c) - 1
                juego.marcar(f, c)
            except:
                print("Formato incorrecto. Usa: marcar fila columna")
            continue

        try:
            f, c = map(int, entrada.split())
            f -= 1
            c -= 1
        except:
            print("Formato incorrecto. Usa: fila columna")
            continue

        juego.descubrir(f, c)
        

    print("\n=== TABLERO FINAL ===")
    for fila in juego.tablero_visible:
        print(" ".join(fila))

    if juego.gano:
        print("\n ¡VICTORIA!")
    else:
        print("\n DERROTA. Piensa mejor la próxima vez.")

def main():
    while True:
        filas, columnas, minas = elegir_dificultad()
        jugar_partida(filas, columnas, minas)

        opcion = input("\n¿Quieres jugar otra partida? (s/n): ").lower()
        if opcion != "s":
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    main()
