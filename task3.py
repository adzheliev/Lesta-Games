"""
В данном модуле приводится функция сортировки массива чисел.
"""
import random


def qsort(arr: list[int]) -> list[int]:
    """Алгоритм быстрой сортировки"""
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lo = [x for x in arr[1:] if x <= pivot]
    hi = [x for x in arr[1:] if x > pivot]
    return qsort(lo) + [pivot] + qsort(hi)


print(qsort([random.randint(1, 100) for _ in range(10)]))
