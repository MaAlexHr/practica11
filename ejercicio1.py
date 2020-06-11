"""
Programador Hernandez Rojas Mara Alexandra Practica 11
Este programa encuentra una contraseña utilizando la

    Estrategia de busqueda de fuerza bruta
    Realiza una busqueda exahustiva

"""
from string import ascii_letters, digits
from itertools import product
from time import time

caracteres = ascii_letters + digits

def buscar(con):
	#Abriri el archivo con las cadenas generadas
	archivo = open("combinaciones.txt","w")
	
	if 3<= len(con) <= 4:
		for i in range(3, 5):
			for comb in product(caracteres, repeat = i):
				prueba ="".join(comb)
				archivo.write(prueba+"\n")
				if prueba == con:
					print("La contraseña es {}".format(prueba))
					break
		archivo.close()
	else:
		print("Ingresa una contraseña de longitud 3 o 4")


if __name__ == "__main__":

	con = input("Ingresa una contraseña\n")
	to = time()
	buscar(con)
	print("Tiempo de ejecucion{} [s]".format(round(time()-to,6)))

"""
Lo que hace time es guardar la hora del momento en el que lo mandan a llamar
Digamos que to es 3:12:06 y en la linea 37 que la vuelve a llamar es 3:12:16
entonces resta (3:12:16)-(3:12:06) = 10[s] 
"""
