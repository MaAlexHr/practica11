"""
Programador Hernandez Rojas Mara Alexandra Practica 11
Grafica que muestra la cantidad de iteracciones de la funcion insertsort
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

times = 0

def insertSort(lista):
    global times
    for i in range(1, len(lista)):
        times += 1
        actual = lista[i]
        posicion = i
        while posicion > 0 and lista[posicion-1] > actual:
            times += 1
            lista[posicion-1] = lista[posicion-1]
            posicion = posicion-1
        lista[posicion] = actual
    return lista

TAM = 101
eje_x = list(range(1, TAM, 1))
eje_y = []

lista_variable=[]

for num in eje_x:
    lista_variable = random.sample(range(0,1000),num)
    times = 0
    lista_variable = insertSort(lista_variable)
    eje_y.append(times)

fig, ax = plt.subplots(facecolor='w', edgecolor='k')
ax.plot(eje_x, eje_y, marker="o", color="g", linestyle="None")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)
ax.legend("Insert Sort")

plt.title("Iteraciones InsertSort")
plt.show()
