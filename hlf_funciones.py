import numpy as np
import random

def comprobar_casillas_h(tamaño:int, tablero:np.ndarray, fila:int, columna:int, prov_list:list):
    for i in range(0,tamaño):
        #comprobamos las casillas donde irá el barco                            
        prov_list.append(tablero[fila][columna+i])
        try:
            #comprobamos las casillas por encima
            prov_list.append(tablero[fila - 1][columna + i])
        except: pass
        try:
            #comprobamos las casillas por debajo
            prov_list.append(tablero[fila + 1][columna + i])
        except: pass
        try:
            #comprobamos la casilla a la izquierda
            prov_list.append(tablero[fila][columna - 1])
        except: pass
        try:
            #comprobamos la casilla arriba a la izquierda
            prov_list.append(tablero[fila - 1][columna - 1])
        except: pass
        try:
            #comprobamos la casilla abajo a la izquierda
            prov_list.append(tablero[fila + 1][columna - 1])
        except: pass
        try:
            #comprobamos la casilla a la derecha
            prov_list.append(tablero[fila][columna + 1 + i])
        except: pass
        try:
            #comprobamos la casilla arriba a la derecha
            prov_list.append(tablero[fila - 1][columna + 1 + i])
        except: pass
        try:
            #comprobamos la casilla abajo a la derecha
            prov_list.append(tablero[fila + 1][columna + 1 + i])
        except: pass

def comprobar_casillas_v(tamaño:int, tablero:np.ndarray, fila:int, columna:int, prov_list:list):
    for i in range(0,tamaño):
        prov_list.append(tablero[fila + i][columna])
        try:
            #comprobamos las casillas por la derecha
            prov_list.append(tablero[fila + i][columna + 1])
        except: pass
        try:
            #comprobamos las casillas por la izquierda
            prov_list.append(tablero[fila + i][columna - 1])
        except: pass
        try:
            #comprobamos la casilla arriba
            prov_list.append(tablero[fila - 1][columna])
        except: pass
        try:
            #comprobamos la casilla arriba a la izquierda
            prov_list.append(tablero[fila - 1][columna - 1])
        except: pass
        try:
            #comprobamos la casilla arriba a la derecha
            prov_list.append(tablero[fila - 1][columna + 1])
        except: pass
        try:
            #comprobamos la casilla por debajo
            prov_list.append(tablero[fila + 1 + i][columna])
        except: pass
        try:
            #comprobamos la casilla abajo a la izquierda
            prov_list.append(tablero[fila + 1 + i][columna - 1])
        except: pass
        try:
            #comprobamos la casilla abajo a la derecha
            prov_list.append(tablero[fila + 1 + i][columna + 1])
        except: pass

def posicionar_barco(tamaño:int, tablero:np.ndarray):
    orientacion = random.randint(0,1)
    prov_list = []
    if orientacion == 0: #horizontal
        #generamos una posición aleatoria de la que partir
        fila = random.randint(0, 9)
        columna = random.randint(0, 10-tamaño)
        #comprobamos casillas de acuerdo al tamaño del barco y las vamos metiendo en la lista prov_list
        comprobar_casillas_h(tamaño, tablero, fila, columna, prov_list)
        if 'O' in prov_list:
            posicionar_barco(tamaño, tablero)
        else:
            for i in range(0,tamaño):
                tablero[fila][columna + i] = "O"
    elif orientacion == 1: #vertical
        fila = random.randint(0, 10-tamaño)
        columna = random.randint(0, 9)
        comprobar_casillas_v(tamaño, tablero, fila, columna, prov_list)
        #comprobamos casillas de acuerdo al tamaño del barco y las vamos metiendo en la lista prov_list
        if 'O' in prov_list:
            posicionar_barco(tamaño, tablero)
        else:
            for i in range(0,tamaño):
                tablero[fila + i][columna] = "O"
    return tablero

def crear_tablero_full():
    tablero = np.full((10,10), " ")
    posicionar_barco(2, tablero)
    posicionar_barco(2, tablero)
    posicionar_barco(3, tablero)
    posicionar_barco(3, tablero)
    posicionar_barco(4, tablero)
    posicionar_barco(1, tablero)
    posicionar_barco(1, tablero)
    return tablero

def crear_tablero_demo():
    tablero = np.full((10,10), " ")
    posicionar_barco(2, tablero)
    posicionar_barco(3, tablero)
    posicionar_barco(4, tablero)
    return tablero

def disparo_aleatorio(tablero_jugador:np.ndarray, tablero_maquina:np.ndarray, jugador:str):
    print(f"Es el turno de la máquina\nTABLERO {jugador.upper()}")
    print(tablero_jugador)
    print("TABLERO MAQUINA")
    print(tablero_maquina)
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    target = tablero_jugador[a][b]
    if target == ' ':
        tablero_jugador[a][b] = '-'
        print("Máquina: ¡agua!")
    elif target == 'O':
        tablero_jugador[a][b] = 'X'
        print("Máquina: ¡tocado!")
        if 'O' not in tablero_jugador:
            return None
        return disparo_aleatorio(tablero_jugador, tablero_maquina, jugador)
    elif target == '-' or target == 'X':
        print('La maquina ha elegido un objetivo no válido, va a volver disparar')
        return disparo_aleatorio(tablero_jugador, tablero_maquina, jugador)

def disparo_jugador(tablero_maquina:np.ndarray, tablero_jugador:np.ndarray, jugador:str):
    print(f"TABLERO {jugador.upper()}")
    print(tablero_jugador)
    print("TABLERO MAQUINA")
    print(tablero_maquina)
    print(f"Te toca {jugador}")
    a = int(input("Elige una fila para tu disparo: "))
    b = int(input("Elige una columna para tu disparo: "))
    try:
        target = tablero_maquina[a][b]
    except:
        print('Has disparado fuera del tablero, repite el tiro')
        return disparo_jugador(tablero_maquina, tablero_jugador, jugador)
    if target == ' ':
        tablero_maquina[a][b] = '-'
        print("¡Agua!")
    elif target == 'O':
        tablero_maquina[a][b] = 'X'
        print("¡Tocado!")
        if 'O' not in tablero_maquina:
            return None
        return disparo_jugador(tablero_maquina, tablero_jugador, jugador)
    elif target == '-' or target == 'X':
        print('Has escogido una casilla donde ya habías disparado, prueba otra vez')
        return disparo_jugador(tablero_maquina, tablero_jugador, jugador)
    
def disparo_aleatorio_f(tablero_jugador:np.ndarray, tablero_maquina:np.ndarray, jugador:str):
    print(f"Es el turno de la máquina\nTABLERO {jugador.upper()}")
    print(tablero_jugador)
    print("TABLERO MAQUINA")
    tablero_maquina_visible = tablero_maquina.copy()
    tablero_maquina_visible[tablero_maquina_visible == 'O'] = ' '
    print(tablero_maquina_visible)
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    target = tablero_jugador[a][b]
    if target == ' ':
        tablero_jugador[a][b] = '-'
        print("Máquina: ¡agua!")
    elif target == 'O':
        tablero_jugador[a][b] = 'X'
        print("Máquina: ¡tocado!")
        if 'O' not in tablero_jugador:
            return None
        return disparo_aleatorio_f(tablero_jugador, tablero_maquina, jugador)
    elif target == '-' or target == 'X':
        print('La maquina ha elegido un objetivo no válido, va a volver disparar')
        return disparo_aleatorio_f(tablero_jugador, tablero_maquina, jugador)
    
def disparo_jugador_f(tablero_maquina:np.ndarray, tablero_jugador:np.ndarray, jugador:str):
    print(f"TABLERO {jugador.upper()}")
    print(tablero_jugador)
    print("TABLERO MAQUINA")
    tablero_maquina_visible = tablero_maquina.copy()
    tablero_maquina_visible[tablero_maquina_visible == 'O'] = ' '
    print(tablero_maquina_visible)
    print(f"Te toca {jugador}")
    a = int(input("Elige una fila para tu disparo: "))
    b = int(input("Elige una columna para tu disparo: "))
    try:
        target = tablero_maquina[a][b]
    except:
        print('Has disparado fuera del tablero, repite el tiro')
        return disparo_jugador_f(tablero_maquina, tablero_jugador, jugador)
    if target == ' ':
        tablero_maquina[a][b] = '-'
        print("¡Agua!")
    elif target == 'O':
        tablero_maquina[a][b] = 'X'
        print("¡Tocado!")
        if 'O' not in tablero_maquina:
            return None
        return disparo_jugador_f(tablero_maquina, tablero_jugador, jugador)
    elif target == '-' or target == 'X':
        print('Has escogido una casilla donde ya habías disparado, prueba otra vez')
        return disparo_jugador_f(tablero_maquina, tablero_jugador, jugador)