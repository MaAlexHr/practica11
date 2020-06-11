"""
Programador Hernandez Rojas Mara Alexandra Practica 12

Vamos a medir teimpos de ejecucion de las funciones quicksort e insertsort y graficarlos
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from time import time
from ejercicio5 import insertSort
from ejercicio6 import quicksort

datos = [ii*100 for ii in range(1, 21)]
tiempo_is = []#tiempo insersort inicializado como una lista vaciia
tiempo_qs = []

for ii in datos:
    lista_is = random.sample(range(0,10000000), ii)#Genera datos aleatorios para ingresar a insersort
    lista_qs = lista_is.copy()

    t0 = time()
    insertSort(lista_is)
    tiempo_is.append(round(time()-t0,6))


    t0 = time()
    quicksort(lista_qs)
    tiempo_qs.append(round(time()-t0,6))

print("Tiempos paciales de ejecucion en Insert Sort {} [s]".format(tiempo_is))
#generando la gráfica imprimimos
print("Tiempos paciales de ejecucion en Quick Sort {} [s]".format(tiempo_qs))

fig, ax = plt.subplots()
ax.plot(datos, tiempo_is, label="insert sort", marker="*", color="r")
ax.plot(datos, tiempo_qs, label="quick sort", marker="o", color="b")
ax.set_xlabel("Datos")
ax.set_ylabel("Tiempo")
ax.grid(True)
ax.legend(loc=2)

plt.title("Tiempos de ejecucion [s] insertSort & quickSort")
plt.show()
