"""
Programdor Hernandez Rojas Mara Alexandra Practica 11
Este programa busca una forma de dar cambio utilizando la estrategia
    algoritmo greedy o Voraz
    Prueba todo lo que tiene pero de acuerdo a un criterio que le garantize un
    beneficio alto y una solución optima aunque no está obligdo a dar con la 
    mejorsolución
"""

def cambio(cantidad, monedas):
	resultado = []
	while cantidad >0:
		if cantidad >= monedas[0]:
			num = cantidad//monedas[0]
			cantidad = cantidad - (num*monedas[0])
			resultado.append([monedas[0],num])
		monedas = monedas[1:]
	return resultado


if __name__ == "__main__":

    print("El cambio se lee [moneda, cantidad]")
    print("Cambio de 1000")
    print(cambio(1000, [20, 10, 5, 2, 1]))
    print("Cambio de 50")
    print(cambio(50, [20, 10, 5, 2, 1]))
    print("Cambio de 37")
    print(cambio(37, [20, 10, 5, 2, 1]))
    print("Cambio de 98 cuando las monedas estan ordenadas de mayor denominacion a menor denominacion")
    print(cambio(98, [20, 10, 5, 2, 1]))
    print("Cambio de 98 con la monedas mal ordenadas")
    print(cambio(98, [5, 20, 1, 50]))

"""
La ultima solucion no es la mas eficiente porque alteramos el orden de las monedas y la lógica del programa no contemplaba un cambio similar
"""
