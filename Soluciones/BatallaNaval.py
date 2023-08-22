import numpy as np

# Crear un tablero de juego 5x5
def crearTablero(Tam):
    tablero = np.zeros((Tam,Tam))
    return tablero
board = np.zeros((5, 5), dtype=int)

# Colocar tres barcos en posiciones aleatorias
def colocarBarcos(tab,cant): 
    #x, y = np.random.randint(0, 5, size=2)
    for _ in cant (3):
        x, y = np.random.randint(0, 5, size=2)
        board[x, y] = 1
 
    print(f"Los valores de x e y son (x , (y)")
# Función para verificar si hay un barco o agua en las coordenadas dadas
def verificarBarco (x, y,tab):
    if tab [x, y] == 1:
        print("¡Has golpeado un barco!")
    
        
    else:
        print("¡El disparo cayó al agua!")

# Prueba la función con algunas coordenadas
verificarBarco(0, 0)
verificarBarco(1, 3)

#Programa>> a JUGAR!
tab = crearTablero()
print("Tablero INICIAL\n")
print(tab)
