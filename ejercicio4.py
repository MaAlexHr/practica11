"""
Programador Hernandez Rojas Mara Alexandra Práctica 11
Este progrma calcula la serie de fibonacci de una forma distinta con:

Estrategia top-down / arriba-abajo / programacion descendente

La diferencia:
    Aquí si se presenta una forma recursiva y nos vamos a ayudar de una 
    función para calcular el dato que me interesa, en caso de que no halla 
    sido calculado lo calculamos sino lo vamos a tomar prestado
"""
memoria = {1:1, 2:1, 3:2}

def fibonacci(numero):
	a = 1
	b = 1
	for i in range (1, numero-1):
		a, b = b, a+b
	return b

def fibonacci_top_down(numero):
	if numero in memoria:
		return memoria[numero]
	f = fibonacci(numero-1) + fibonacci(numero-2)
	memoria[numero] = f
	return memoria[numero]

if __name__ == "__main__":

    print(fibonacci_top_down(5))
    print(memoria)
    print(fibonacci_top_down(4))
    print(memoria)
    print(fibonacci_top_down(8))
    print(memoria)
    print(fibonacci_top_down(6))
