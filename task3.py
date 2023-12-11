"""
В данном модуле приводятся функции сортировки массива чисел.
"""
import random


def standard_sort(arr: list[int]) -> list[int]:
    """Стандартная функция сортировки"""
    return sorted(arr)


def qsort(arr: list[int]) -> list[int]:
    """Алгоритм быстрой сортировки"""
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lo = [x for x in arr[1:] if x <= pivot]
    hi = [x for x in arr[1:] if x > pivot]
    return qsort(lo) + [pivot] + qsort(hi)


print(standard_sort([random.randint(1, 100) for _ in range(10)]))
print(qsort([random.randint(1, 100) for _ in range(10)]))
