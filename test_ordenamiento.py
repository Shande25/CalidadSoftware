import pytest
from ordenamiento import bubble_sort, seleccion_sort, insertion_sort, merge_sort, quick_sort

# Bubble Sort Tests
def test_bubble_sort_case1():
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bubble_sort(arr[:]) == [11, 12, 22, 25, 34, 64, 90]

def test_bubble_sort_case2():
    arr = [5, 4, 3, 2, 1]
    assert bubble_sort(arr[:]) == [1, 2, 3, 4, 5]

def test_bubble_sort_case3():
    arr = [3, 1, 2, 3, 1, 2]
    assert bubble_sort(arr[:]) == [1, 1, 2, 2, 3, 3]

# Selection Sort Tests
def test_seleccion_sort_case1():
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert seleccion_sort(arr[:]) == [11, 12, 22, 25, 34, 64, 90]

def test_seleccion_sort_case2():
    arr = []
    assert seleccion_sort(arr[:]) == []

def test_seleccion_sort_case3():
    arr = [5]
    assert seleccion_sort(arr[:]) == [5]

# Insertion Sort Tests
def test_insertion_sort_case1():
    arr = [1, 2, 3, 4, 5]
    assert insertion_sort(arr[:]) == [1, 2, 3, 4, 5]

def test_insertion_sort_case2():
    arr = [5, 4, 3, 2, 1]
    assert insertion_sort(arr[:]) == [1, 2, 3, 4, 5]

def test_insertion_sort_case3():
    arr = [3, -1, 2, -3, 1, 0]
    assert insertion_sort(arr[:]) == [-3, -1, 0, 1, 2, 3]

# Merge Sort Tests
def test_merge_sort_case1():
    arr = [64, 34, 25, 12, 22, 11, 90]
    merge_sort(arr)
    assert arr == [11, 12, 22, 25, 34, 64, 90]

def test_merge_sort_case2():
    arr = []
    merge_sort(arr)
    assert arr == []

def test_merge_sort_case3():
    arr = [5, 4, 3, 2, 1]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

# Quick Sort Tests
def test_quick_sort_case1():
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert quick_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_quick_sort_case2():
    arr = []
    assert quick_sort(arr) == []

def test_quick_sort_case3():
    arr = [5, 4, 3, 2, 1]
    assert quick_sort(arr) == [1, 2, 3, 4, 5]
