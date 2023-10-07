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
    '''if tamaño == 1:
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        #comprobamos si ha elegido una posición en la que ya hay un barco
        if tablero[fila][columna] == "O":
            posicionar_barco(tamaño, tablero)
        else:
            try:
                #comprobamos la casilla por encima
                prov_list.append(tablero[fila - 1][columna])
            except: pass
            try:
                #comprobamos la casilla por debajo
                prov_list.append(tablero[fila + 1][columna])
            except: pass
            try:
                #comprobamos la casilla a la derecha
                prov_list.append(tablero[fila][columna + 1])
            except: pass
            try:
                #comprobamos la casilla a la izquierda
                prov_list.append(tablero[fila][columna - 1])
            except: pass
            try:
                #comprobamos la casilla arriba a la derecha
                prov_list.append(tablero[fila - 1][columna + 1])
            except: pass
            try:
                #comprobamos la casilla arriba a la izquierda
                prov_list.append(tablero[fila - 1][columna - 1])
            except: pass
            try:
                #comprobamos la casilla abajo a la derecha
                prov_list.append(tablero[fila + 1][columna + 1])
            except: pass
            try:
                #comprobamos la casilla abajo a la izquierda
                prov_list.append(tablero[fila + 1][columna - 1])
            except: pass
            if 'O' in prov_list:
                posicionar_barco(tamaño, tablero)
            else:
                tablero[fila][columna] = "O"
            return tablero'''
    if orientacion == 0: #horizontal
        #generamos una posición aleatoria de la que partir
        fila = random.randint(0, 9)
        columna = random.randint(0, 10-tamaño)
        #comprobamos casillas de acuerdo al tamaño del barco y las vamos metiendo en la lista prov_list
        comprobar_casillas_h(tamaño, tablero, fila, columna, prov_list)
        '''for i in range(0,tamaño):
            #comprobamos las casillas donde irá el barco                            
            prov_list.append(tablero[fila][columna+i])
            try:
                #comprobamos las casillas por encima
                prov_list.append(tablero[fila - 1][columna+i])
            except: pass
            try:
                #comprobamos las casillas por debajo
                prov_list.append(tablero[fila + 1][columna+i])
            except: pass
            #comprobamos casos para la primera casilla
            if i == 0:
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
            #comprobamos casos para la última casilla
            elif i == tamaño - 1:
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
                except: pass'''
        if 'O' in prov_list:
            posicionar_barco(tamaño, tablero)
        else:
            for i in range(0,tamaño):
                tablero[fila][columna+i] = "O"
    elif orientacion == 1: #vertical
        fila = random.randint(0, 10-tamaño)
        columna = random.randint(0, 9)
        comprobar_casillas_v(tamaño, tablero, fila, columna, prov_list)
        #comprobamos casillas de acuerdo al tamaño del barco y las vamos metiendo en la lista prov_list
        '''for i in range(0,tamaño):
            prov_list.append(tablero[fila+i][columna])
            try:
                #comprobamos las casillas por la derecha
                prov_list.append(tablero[fila+i][columna+1])
            except: pass
            try:
                #comprobamos las casillas por la izquierda
                prov_list.append(tablero[fila+i][columna-1])
            except: pass
            #comprobamos casos para la primera casilla
            if i == 0:
                try:
                    #comprobamos la casilla arriba
                    prov_list.append(tablero[fila-1][columna])
                except: pass
                try:
                    #comprobamos la casilla arriba a la izquierda
                    prov_list.append(tablero[fila-1][columna - 1])
                except: pass
                try:
                    #comprobamos la casilla arriba a la derecha
                    prov_list.append(tablero[fila-1][columna + 1])
                except: pass
            #comprobamos casos para la última casilla
            elif i == tamaño - 1:
                try:
                    #comprobamos la casilla por debajo
                    prov_list.append(tablero[fila + i + 1][columna])
                except: pass
                try:
                    #comprobamos la casilla abajo a la izquierda
                    prov_list.append(tablero[fila + i + 1][columna - 1])
                except: pass
                try:
                    #comprobamos la casilla abajo a la derecha
                    prov_list.append(tablero[fila + i + 1][columna + 1])
                except: pass'''
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

def disparo_aleatorio(tablero_jugador:np.ndarray):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    target = tablero_jugador[a][b]
    if target == ' ':
        tablero_jugador[a][b] = '-'
        print("Turno de la máquina: ¡agua!")
        return False
    elif target == 'O':
        tablero_jugador[a][b] = 'X'
        print("Turno de la máquina: ¡tocado!")
        return True
    elif target == '-' or target == 'X':
        print('La maquina ha elegido un objetivo no valido, va a volver disparar')
        return disparo_aleatorio(tablero_jugador)

def disparo_jugador(tablero_maquina:np.ndarray):
    a = int(input("Elige una fila para tu disparo: "))
    b = int(input("Elige una columna para tu disparo: "))
    try:
        target = tablero_maquina[a][b]
    except:
        print('Has disparado fuera del tablero, repite el tiro')
        return disparo_jugador(tablero_maquina)
    if target == ' ':
        tablero_maquina[a][b] = '-'
        print("¡Agua!")
        return False
    elif target == 'O':
        tablero_maquina[a][b] = 'X'
        print("¡Tocado!")
        return True
    elif target == '-' or target == 'X':
        print('Has escogido una casilla donde ya habías disparado, prueba otra vez')
        return disparo_jugador(tablero_maquina)