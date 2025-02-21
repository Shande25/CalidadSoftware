import pytest
from ordenamiento import bubble_sort, seleccion_sort, insertion_sort, merge_sort, quick_sort

# Bubble Sort Tests
@pytest.mark.parametrize("arr, esperado", [
    ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 3, 1, 2], [1, 1, 2, 2, 3, 3])
])
def test_bubble_sort(arr, esperado):
    assert bubble_sort(arr[:]) == esperado

# Selection Sort Tests
@pytest.mark.parametrize("arr, esperado", [
    ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
    ([], []),
    ([5], [5])
])
def test_seleccion_sort(arr, esperado):
    assert seleccion_sort(arr[:]) == esperado

# Insertion Sort Tests
@pytest.mark.parametrize("arr, esperado", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([3, -1, 2, -3, 1, 0], [-3, -1, 0, 1, 2, 3])
])
def test_insertion_sort(arr, esperado):
    assert insertion_sort(arr[:]) == esperado

# Merge Sort Tests
@pytest.mark.parametrize("arr, esperado", [
    ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
    ([], []),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
])
def test_merge_sort(arr, esperado):
    merge_sort(arr)
    assert arr == esperado

# Quick Sort Tests
@pytest.mark.parametrize("arr, esperado", [
    ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
    ([], []),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
])
def test_quick_sort(arr, esperado):
    assert quick_sort(arr) == esperado
