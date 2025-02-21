import pytest
from busqueda import busqueda_lineal, busqueda_binaria_iterativa, busqueda_binaria_recursiva

arr_desordenado = [64, 34, 25, 12, 22, 11, 90]
arr_ordenado = sorted(arr_desordenado)
arr_vacio = []

@pytest.mark.parametrize("arr, elemento, esperado", [
    (arr_desordenado, 22, True),  
    (arr_desordenado, 100, False),  
    (arr_vacio, 22, False)  
])
def test_busqueda_lineal(arr, elemento, esperado):
    assert (busqueda_lineal(arr, elemento) != -1) == esperado

@pytest.mark.parametrize("arr, elemento, esperado", [
    (arr_ordenado, 22, True),  
    (arr_ordenado, 100, False),  
    (arr_vacio, 22, False)  
])
def test_busqueda_binaria_iterativa(arr, elemento, esperado):
    assert (busqueda_binaria_iterativa(arr, elemento) != -1) == esperado

@pytest.mark.parametrize("arr, elemento, esperado", [
    (arr_ordenado, 22, True),  
    (arr_ordenado, 100, False),  
    (arr_vacio, 22, False)  
])
def test_busqueda_binaria_recursiva(arr, elemento, esperado):
    assert (busqueda_binaria_recursiva(arr, elemento, 0, len(arr) - 1) != -1) == esperado
