import os
import random
import time
from tablero_hundir_la_flota import crear_tablero, mostrar_tableros_paralelos, colocar_barcos_con_registro
import juego as logica

# Configuración: Nombre del barco y su longitud
BARCOS_A_COLOCAR = {
    "Portaaviones": 4, 
    "Acorazado": 3, 
    "Destructor": 2, 
    "Fragata": 1
}

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    limpiar_pantalla()
    print("================================")
    print("   BIENVENIDO A HUNDIR LA FLOTA ")
    print("================================")
    
    try:
        tam = int(input("\nElige el tamaño del tablero (5-15, default 10): "))
        if not (5 <= tam <= 15): tam = 10
    except:
        tam = 10

    # Inicialización de tableros
    mi_tablero = crear_tablero(tam)
    mis_disparos = crear_tablero(tam)
    cpu_tablero_oculto = crear_tablero(tam)
    cpu_disparos_vistos = crear_tablero(tam) # Para que la CPU no repita tiros

    # Colocación de barcos con registro de coordenadas
    mis_barcos = colocar_barcos_con_registro(mi_tablero, BARCOS_A_COLOCAR)
    cpu_barcos = colocar_barcos_con_registro(cpu_tablero_oculto, BARCOS_A_COLOCAR)

    while True:
        limpiar_pantalla()
        mostrar_tableros_paralelos(mi_tablero, mis_disparos)
        print(f"\nBarcos enemigos restantes: {len(cpu_barcos)}")
        
        
        # Turno del jugador
        turno_valido = False
        while not turno_valido:
            try:
                coord = input("\nTu disparo (ej. A5): ").upper()
                f = ord(coord[0]) - 65
                c = int(coord[1:])
                
                res = logica.procesar_disparo(cpu_tablero_oculto, mis_disparos, f, c)
                
                if res == "FUERA":
                    print("Coordenadas fuera del mapa.")
                elif res == "REPETIDO":
                    print("Ya has disparado ahí, intentalo otra vez.")
                else:
                    print(f"Resultado: ¡{res}!")
                    nombre_hundido = logica.verificar_hundimiento(mis_disparos, cpu_barcos)
                    if nombre_hundido:
                        print(f"Has hundido el {nombre_hundido} enemigo.")
                    turno_valido = True
            except:
                print("Formato inválido. Usa Letra+Número (ej. B3).")

        if logica.hay_ganador(cpu_barcos):
            limpiar_pantalla()
            mostrar_tableros_paralelos(mi_tablero, mis_disparos)
            print("\n¡VICTORIA! Has hundido toda la flota enemiga.")
            break
        
        # Turno de la CPU
        print("\nPensando...")
        time.sleep(1)
        
        cpu_hizo_tiro = False
        while not cpu_hizo_tiro:
            cf, cc = random.randint(0, tam-1), random.randint(0, tam-1)
            res_cpu = logica.procesar_disparo(mi_tablero, cpu_disparos_vistos, cf, cc)
            if res_cpu != "REPETIDO":
                # Aplicamos el visual del tiro de la CPU en nuestro tablero
                if res_cpu == "TOCADO":
                    mi_tablero[cf][cc] = "X"
                    nombre_hundido_cpu = logica.verificar_hundimiento(cpu_disparos_vistos, mis_barcos)
                    if nombre_hundido_cpu:
                        print(f"La CPU ha hundido tu {nombre_hundido_cpu}...")
                else:
                    mi_tablero[cf][cc] = "O"
                cpu_hizo_tiro = True

        if logica.hay_ganador(mis_barcos):
            limpiar_pantalla()
            mostrar_tableros_paralelos(mi_tablero, mis_disparos)
            print("\nDERROTA... La flota enemiga te ha destruido.")
            break
            
        input("\nPresiona Enter para el siguiente turno...")

if __name__ == "__main__":
    main()