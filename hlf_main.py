from hlf_funciones import *

print('Bienvenido a hundir la flota, una aventura llena de emoción y gráficos hiperrealistas')

jugador:str = input('Introduce tu nombre: ')

game_mode = input('Elige el modo de juego:\n- Para jugar a la demo pulsa 1\n- Para jugar a la version completa pulsa 2\n')
while game_mode not in ['1','2']:
    game_mode = input('El número introducido no es válido, vuelve a intentarlo\n')

print('\n¡Comienza el juego!\n')

if game_mode == '1':

    tablero_maquina = crear_tablero_demo()
    tablero_jugador = crear_tablero_demo()

    while ("O" in tablero_jugador) or ("O" in tablero_maquina):
        disparo_jugador(tablero_maquina, tablero_jugador, jugador)
        if "O" not in tablero_maquina:
            break
        disparo_aleatorio(tablero_jugador, tablero_maquina, jugador)

elif game_mode == '2':
    
    tablero_maquina = crear_tablero_full()
    tablero_jugador = crear_tablero_full()

    while ("O" in tablero_jugador) or ("O" in tablero_maquina):
        disparo_jugador_f(tablero_maquina, tablero_jugador, jugador)
        if "O" not in tablero_maquina:
            break
        disparo_aleatorio_f(tablero_jugador, tablero_maquina, jugador)

print(f"TABLERO {jugador.upper()}")
print(tablero_jugador)
print("TABLERO MAQUINA")
print(tablero_maquina)
if "O" not in tablero_jugador: 
    print(f"Mala suerte {jugador}, ¡has perdido!")
elif "O" not in tablero_maquina:
    print(f"Enhorabuena {jugador}, ¡has ganado!")