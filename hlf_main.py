from hlf_funciones import *

print('Bienvenido a hundir la flota, una aventura llena de emoción y gráficos hiperrealistas')

jugador = input('Introduce tu nombre: ')

game_mode = input('Elige el modo de juego: \n- Para jugar a la demo pulsa 1 \n- Para jugar a la version completa pulsa 2\n')
while game_mode not in ['1','2']:
    game_mode = input('El número introducido no es válido, vuelve a intentarlo \n')

print('\n¡Comienza el juego!\n')

if game_mode == '1':

    tablero_maquina = crear_tablero_demo()
    tablero_jugador = crear_tablero_demo()

    while ("O" in tablero_jugador) or ("O" in tablero_maquina):
        while True:
            print("TABLERO JUGADOR")
            print(tablero_jugador)
            print("TABLERO MAQUINA")
            print(tablero_maquina)
            print(f"Te toca {jugador}")
            tocado = disparo_jugador(tablero_maquina)
            if tocado == False or "O" not in tablero_maquina:
                break
        if "O" not in tablero_maquina:
            break
        while True:
            print("Es el turno de la máquina \nTABLERO JUGADOR")
            print(tablero_jugador)
            print("TABLERO MAQUINA")
            print(tablero_maquina)
            tocado = disparo_aleatorio(tablero_jugador)
            if tocado == False or 'O' not in tablero_jugador:
                break

    print("TABLERO JUGADOR")
    print(tablero_jugador)
    print("TABLERO MAQUINA")
    print(tablero_maquina)
    if "O" not in tablero_jugador: 
        print("¡Has perdido!")
    elif "O" not in tablero_maquina:
        print("¡Has ganado!")

elif game_mode == '2':
    tablero_maquina = crear_tablero_full()
    tablero_jugador = crear_tablero_full()

    while ("O" in tablero_jugador) or ("O" in tablero_maquina):
        while True:
            print("TABLERO JUGADOR")
            print(tablero_jugador)
            print("TABLERO MAQUINA")
            tablero_maquina_visible = tablero_maquina.copy()
            tablero_maquina_visible[tablero_maquina_visible == 'O'] = ' '
            print(tablero_maquina_visible)
            print(f"Te toca {jugador}")
            tocado = disparo_jugador(tablero_maquina)
            if tocado == False or "O" not in tablero_maquina:
                break
        if "O" not in tablero_maquina:
            break
        while True:
            print("Es el turno de la máquina \nTABLERO JUGADOR")
            print(tablero_jugador)
            print("TABLERO MAQUINA")
            tablero_maquina_visible = tablero_maquina.copy()
            tablero_maquina_visible[tablero_maquina_visible == 'O'] = ' '
            print(tablero_maquina_visible)
            tocado = disparo_aleatorio(tablero_jugador)
            if tocado == False or 'O' not in tablero_jugador:
                break

    print("TABLERO JUGADOR")
    print(tablero_jugador)
    print("TABLERO MAQUINA")
    print(tablero_maquina)
    if "O" not in tablero_jugador: 
        print("¡Has perdido!")
    elif "O" not in tablero_maquina:
        print("¡Has ganado!")