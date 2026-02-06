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
