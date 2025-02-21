import time 
import numpy as np

def get_firt_element(arr):
    return arr[0]


def busqueda_lineal(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
def busqueda_binaria(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1



def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

    from itertools import permutations

def all_permutations(arr):
    return list(permutations([1, 2, 3]))



np.random.seed(42)
arr = np.random.randint(1, 100, size=10000)

#Complejidad Constante
inicio = time.time()
print(get_firt_element(arr))
fin = time.time()
print(f"Tiempo de ejecucion constante:{fin-inicio}segunos")

#Complejidad Lineal
inicio = time.time()
arr.sort()
print(busqueda_lineal(arr, 42))
fin = time.time()
print(f"Tiempo de ejecucion constante:{fin-inicio}segunos")


#Complejidad Cuadratica
arr = np.random.randint(1, 100, size=100)
inicio = time.time()
bubble_sort(arr)
fin = time.time()
print(f"Tiempo de ejecucion bubble sort:{fin-inicio}segunos")


#Complejidad lineal - logaritmica
arr = np.random.randint(1, 100, size=100)
inicio = time.time()
merge_sort(arr)
fin = time.time()
print(f"Tiempo de ejecucion merge sort:{fin-inicio}segunos")



# Complejidad exponencial
inicio = time.time()
fibonacci(40)
fin = time.time()
print(f"Tiempo de ejecucion fibonacci:{fin-inicio}segunos")


# Complejidad factorial
inicio = time.time()
print(all_permutations([1, 2, 3]))
fin = time.time()
print(f"Tiempo de ejecucion factorial:{fin-inicio}segunos")