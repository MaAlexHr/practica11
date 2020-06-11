""""
Programador Hernandez Rojas MAra Alexandra Practica 11
El programa ordena numeros de mayo a menor con QuickSort 
    es de tipo DIVIDE Y VENCERAS toma un problema y lo secciona en problemas mas    pequeños y faciles de resolver

Lo primero que buscas es un valor pibote y mueves los valores en posición incorrecta a la correcta con respecto del pibote
Tenemos la lista desordenada
21 10 12 0 34 15
Elegimos un pibote p=21
El que esta a su derecha es el primero
El que esta a su izquierda es el ultimo que se recorre lo más que se pueda 
mientras el pibote sea mayor que izquierda se va a ir recorriendo
21 10 12 0 34 15
p   i          d
21 10 12 0 34 15
p           i  d

Entre mejor sea el pibote mas efectivo es el codigo es decir 
¿i>21? NO		¿d<21? SI
Intercambiamos el pibote con d
15 10 12 0 34 21
p  i           d
Y recorremos d
15 10 12 0 34 21
p  i       d
¿i<
Cuando se cruzan los indices se dividen las listas y se selecciona un nuevo pibote

"""

def quicksort(lista):
	quicksort2(lista, 0, len(lista)-1)


def quicksort2(lista, inicio, fin): #esta parte nos pemite dividir el arreglo
	if inicio < fin: #No se han cruzado los indices
		pivote = particion(lista, inicio, fin)
		quicksort2(lista, inicio, pivote-1)
		quicksort2(lista, pivote+1, fin)

def particion(lista, inicio, fin):
	pivote = lista[inicio]
	#print("Valor del pivote {}".format(pivote))
	izquierda = inicio+1
	derecha = fin
	#print("indice izquierda {} indice derecha{} ".format(izquierda,derecha))

	bandera = False

	while not bandera:
		while izquierda <= derecha and lista[izquierda] <= pivote:
			izquierda = izquierda + 1
		while derecha >= izquierda and lista[derecha] >= pivote:
			derecha = derecha-1
			if derecha < izquierda:
				bandera = True
			else:
				temp = lista[izquierda]
				lista[izquierda] = lista[derecha]
				lista[derecha] = temp
		#print(lista)
		temp = lista[inicio]
		lista[inicio] = lista[derecha]
		lista[derecha] = temp
		return derecha

if __name__ == "__main__":

    lista=[21, 10, 12, 0 , 15, 34]
    print("\nLista inicial {}".format(lista))
    quicksort(lista)
    print("\nLista final {}".format(lista))

#Orden O(nlogn)
