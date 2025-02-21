import time

#Ordenamiento por Burbuja
def bubble_sort(arr):
    n = len(arr)
    print(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

#Ordenamiento por Selección 
def seleccion_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#Ordenamiento por Inserción
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1       
        arr[j+1] = key
    return arr

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

def quick_sort(arr):
    n = len(arr)
    if n <= 1: return arr
    pivot = arr[n//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [64, 34, 25, 12, 22, 11, 90]
inicio = time.time()
print(bubble_sort(arr))
fim = time.time()
print(f"Tiempo de ejecución bubble: {fim - inicio} segundos")

arr = [64, 34, 25, 12, 22, 11, 90]
inicio = time.time()
print(seleccion_sort(arr))
fim = time.time()
print(f"Tiempo de ejecución seleccion: {fim - inicio} segundos")

arr = [64, 34, 25, 12, 22, 11, 90]
inicio = time.time()
print(insertion_sort(arr))
fim = time.time()
print(f"Tiempo de ejecución insertion: {fim - inicio} segundos")
