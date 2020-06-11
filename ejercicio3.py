"""
Programador Hernandez Rojas Mara Alexandra Practica 11
Este programa resuelve la serie de fibbonacci de tres maneras distintas

Version iterativa con estructura de for
"""

def fibonacci_a(numero):
	a = 1
	b = 0
	c = 0
	for i in range(1, numero-1):
		c = a + b
		a = b
		b = c
	return c

"""
Version iterativa Asignacion paralela eliminamos a la variable c
"""

def fibonacci_b(numero):
        a = 1
        b = 1
        for i in range(1, numero-1):
                a, b = b, a + b
        return b
"""
Version bottom-up / Abajo->Arriba / progrmación Ascendente
Digagrama de Arbol
                fibonacci(3) = 3
                /           \
        fibonacci(2)  +  fibonacci(1)
         /   2   \            1
fibonacci(1) + fibonacci(0)
    1       +       1

Los resultados parciales se van almacenado en un arreglo que actua como 
memoria temporal
"""

def fibonacci_c(numero):
        fib_parcial = [1, 1, 2]
        while len(fib_parcial) < numero:
                fib_parcial.append(fib_parcial[-1]+fib_parcial[-2])
                print(fib_parcial)
        return fib_parcial[numero-1]

if __name__ == "__main__":
    f = fibonacci_a(0)
    print("\nFibonacci iterativo de 0 = ", f)
    f = fibonacci_b(4)
    print("\nFibonacci iterativo de 4 = ", f)
    f = fibonacci_c(3)
    print("\nFibonacci bottom-up de 3 =", f)
    print("\nComo se llena la memoria con bottom-up")
    f = fibonacci_c(7)
    print("\nFibonacci bottom-up de 7 =", f)
