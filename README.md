# Hundir la flota

Recreación del famoso juego de barcos utilizando **Python** y **Numpy** como base para su programación.

La **lógica del script** funciona de forma análoga al juego original:
1. Distribución de los barcos en cada tablero
2. Disparar seleccionando una casilla
3. Actualizar el estatus de dicha casilla
4. Cambio/Continuación de turno

Las principales **funciones** del script son las siguientes:
- 'Posicionar barco': esta función toma un argumento tablero y otro argumento tamaño. Luego genera una lista vacía ('prov_list') y un número aleatorio (1 ó 0) para decidir la orientación del barco. A continuación, se generan dos números aleatorios para determinar la coordenada donde comenzará a construirse el barco. La orientación y el tamaño se tendrán en cuenta para acotar el área de la matriz en la que el barco no se saldrá al ser colocado. A continuación, se comprueban las casillas donde irá el barco con la función 'comprobar_casillas' (ver más adelante). Ésta creará una lista con los caracteres de las casillas comprobadas. Si en ellas no hay ninguna 'O', el barco se coloca en el tablero. Si la hay, se repite la función
- 'Comprobar casillas': tiene dos versiones, para la orientación vertical y la horizontal. Esta función toma las coordenadas de 'posicionar barco' y añade a la lista 'prov_list' los caracteres del tablero donde irá el barco y los de su alrededor.
- 'Crear tablero': tiene dos versiones, demo y full. Esta función sencillamente genera el tablero de juego con los barcos colocados ejecutando varias veces la función 'posicionar barco'
- 'Disparo aleatorio' y 'Disparo jugador': se generan un par de números del 0 al 9 que representan las coordenadas de la matriz a la que se disparará. Si el caracter de la matriz es una O, se imprime un 'tocado' y se repite la fnción, si es un X o -, se imprime un mensaje de casilla ya elegida y se repite la función, si es una casilla fuera del tablero se imprime un mensaje de aviso y se repite la función, si la casilla es un espacio en blanco se imprime 'agua' y se sale de la función.
- Las versiones 'Disparo aleatorio_f' y 'Disparo jugador_f' aplican una máscara al tablero_maquina que filtra el caracter 'O' y lo sustituye por ' '.

El **bucle principal** es un while que comprueba si quedan caracteres 'O' dentro de los tableros.
Cuando el while general se resuelve, un mensaje de victoria o derrota y los tableros finales.
