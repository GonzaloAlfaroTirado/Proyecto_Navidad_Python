import os
import random
import time
from tablero_hundir_la_flota import crear_tablero, mostrar_tableros_paralelos, colocar_barcos_con_registro
import juego_hundir_la_flota as logica

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