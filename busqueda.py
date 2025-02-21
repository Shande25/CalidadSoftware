
def busqueda_lineal(arr, x):
    for i in range(len(arr)):
        print(i,arr[i],x)
        if arr[i] == x:
            return i
    return -1
def busqueda_binaria_iterativa(arr, x):
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
        print(low,mid,high)
    return -1

def busqueda_binaria_recursiva(arr, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x: return mid
    elif arr[mid] < x:
        return busqueda_binaria_recursiva(arr, x, mid + 1, high)
    else:
        return busqueda_binaria_recursiva(arr, x, low, mid - 1)


arr = [64, 34, 25, 12, 22, 11, 90]
print(busqueda_lineal(arr, 22))
arr.sort()
print(busqueda_binaria_iterativa(arr, 22))
print(busqueda_binaria_recursiva(arr, 22, 0, len(arr) - 1))
