import time

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)

inicio = time.time()
print(factorial_iterative(100))
fin = (time.time() - inicio) 
print(f"Tiempo de ejecución interativo: {fin - inicio} segundos")

inicio = time.time()
print(factorial_recursive(100))
fin = (time.time() - inicio)
print(f"Tiempo de ejecución recursivo: {fin - inicio} segundos")        