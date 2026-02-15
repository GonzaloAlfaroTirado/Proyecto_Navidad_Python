from juego import Juego

def elegir_dificultad():
    print("\n=== SELECCIONA DIFICULTAD ===")
    print("1. Fácil      (8x8, 10 minas)")
    print("2. Medio      (12x12, 20 minas)")
    print("3. Difícil    (16x16, 40 minas)")
    print("4. Personalizado")

    while True:
        opcion = input("\nElige una opción (1-4): ").strip()
        if opcion == "1":
            return 8, 8, 10
        elif opcion == "2":
            return 12, 12, 20
        elif opcion == "3":
            return 16, 16, 40
        elif opcion == "4":
            return pedir_personalizado()
        else:
            print("Opción no válida. Intenta de nuevo.")

def pedir_personalizado():
    print("\n=== MODO PERSONALIZADO ===")
    while True:
        try:
            filas = int(input("Filas: "))
            columnas = int(input("Columnas: "))
            total_casillas = filas * columnas

            if filas <= 0 or columnas <= 0:
                print("Las dimensiones del tablero deben ser mayores que cero.")
                continue

            max_minas = (total_casillas * 3) // 4  # 75% del tablero
            print(f"Máximo de minas permitido: {max_minas}")
            minas = int(input("Minas: "))

            if 1 <= minas <= max_minas:
                return filas, columnas, minas
            else:
                print(f"Las minas deben estar entre 1 y {max_minas}.")
        except:
            print("Introduce números válidos.")
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
            for casilla in fila:
                print(f"{casilla:2}", end=" ") 
            print()

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
