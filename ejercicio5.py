"""
Programador Hernandez Rojas Mara Alexandra Practica 11
Estrategia incrementar hace la solución mas grande y la va probando
        Algoritmo de ordenamiento por inserción
El algoritmo de inserción ordena el elemento manteniendo una sublista 
de numeros ordenados, al principio vamos a considerar que el elemento 
en la primera posición esta ordenado.
Vamos a insertar en la parte ordenada
Primera parte del arreglo
21 10 12 0 34 15
Parte orenada
21		10 12 0 34 15
¿10<21? si
10 21		12 0 34 15
¿12<10? No	recorremos
¿21<21? si
10 12 21	0 34 15
¿0<10? si
0 10 12 21	34 15
¿34<0? no 
...
0 10 12 15 21 34
Comenzamos con una solucion pequeña formada por un numero 
y a la siguiente iteracion crece y crece y crece
"""
def insertSort(lista):
    for index in range(1, len(lista)): #O(n-1)
        actual = lista[index]
        posicion = index
        #print("Valor a ordenar {}".format(actual))
        while posicion>0 and lista[posicion-1]>actual: #O(n^2)
            lista[posicion] = lista[posicion-1]
            posicion = posicion-1
        lista[posicion] = actual
        #print(lista)
    return lista


if __name__ == "__main__":

    lista = [21, 10, 12, 0, 34, 15]                 
    print("Lista Desordenada {} ".format(lista))
    insertSort(lista)
    print("\nLista Ordenada {} ".format(lista))

"""
Orden es O(n**2)
"""

