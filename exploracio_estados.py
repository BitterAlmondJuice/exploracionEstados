import numpy as np
import random

estado_lista = list(range(9))

META = np.array(estado_lista).reshape(3,3)
random.shuffle(estado_lista)
estado_inicial = np.array(estado_lista).reshape(3,3)

print(estado_inicial)

##################################################################################################################

direcciones = {'arriba': (-1, 0),
               'izquierda': (0, 1),
               'derecha': (0, -1),
               'abajo': (1, 0),
               }

def mover(estado, posicion, direccion):         #intercambia dos numeros, el indicado en la posicion y el que toque segun la direccion del intercambio
  nuevo_estado = estado.copy()  #copia la matriz actual
  dir_delta = direcciones[direccion]    #copia el valor a sumar a las coordenadas determinadas
  p_x, p_y = posicion   #guarda la posicion x,y del numero a mover
  d_x, d_y = [x + y for x, y in zip(posicion, dir_delta)]   #la funcion zip() guarda los parametros pasados en una tupla,
                                                              #las coordenadas del numero que toca intercambiar segun la direccion de movimiento del argumento "posicion"
  aux = nuevo_estado[p_x, p_y]      #crea un numero auxiliar que representa el numero pasado por el argumento "posicion"
  nuevo_estado[p_x, p_y] = nuevo_estado[d_x, d_y]       #asigna en la posicion del primer objeto el valor del segundo
  nuevo_estado[d_x, d_y] = aux                          #asigna en la posicion del segundo objeto el valor del auxiliar(lo que viene siendo el objeto pasado por "posicion"), completando el intercambio

  return nuevo_estado       #devuelve el nuevo estado tras el intercambio

"""
codigo equivalente en java:


int[] direcciones(String direccion){

    int[] resultado = [-1, -1];

    switch(direccion){
        case arriba:
            resultado = new int[]{-1, 0};
            break;
        case izquierda:
            resultado = new int[]{0, 1};
            break;
        case derecha:
            resultado = new int[]{0, -1};
            break;
        case abajo:
            resultado = new int[]{1, 0};
            break;
    }

    return resultado;

}

int[][] mover(int[][] estado, int[] posicion, String direccion){

    int[][] nuevo_estado = estado;
    int[] dir_delta = direcciones(direccion);
    p_x = posicion[0];
    p_y = posicion[1];
    d_x = p_x + dir_delta[0];
    d_y = p_y + dir_delta[1];
    int aux = nuevo_estado[p_x, p_y];
    nuevo_estado[p_x, p_y] = nuevo_estado[d_x, d_y];
    nuevo_estado[d_x, d_y] = aux;

    return nuevo_estado;

}


"""
##################################################################################################################
print("¿posicion x?")
posicion_x = int(input())
print("¿posicion y?")
posicion_y = int(input())
posicion = (posicion_x, posicion_y)
print("¿a donde quieres moverlo?")
direccion = input()
nuevo_estado = mover(estado_inicial, posicion, direccion)
print(nuevo_estado)
