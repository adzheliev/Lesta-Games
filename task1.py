"""
В данном модуле приводится альтернативная функция
для определения чётности числа.
"""


def is_even(number: int) -> str | bool:
    """Функция получает на вход значение и пытается преобразовать
    его в int для последующего определения чётности"""
    if not isinstance(number, int):
        try:
            number = int(number)
        except (TypeError, ValueError):
            return f"Value {number} can't be converted"
    if number & 1:
        return False
    return True


def is_even_for_large_numbers(number: int | str) -> str | bool:
    """Функция получает на вход значение и пытается преобразовать
    его в int для последующего определения чётности"""
    try:
        return int(str(number)[-1]) % 2 == 0
    except (TypeError, ValueError):
        return f"Value {number} can't be converted"
