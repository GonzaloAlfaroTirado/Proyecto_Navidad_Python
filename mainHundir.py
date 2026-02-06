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
    
    # Aquí irá la lógica de inicialización...

if __name__ == "__main__":
    main()