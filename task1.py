"""
В данном модуле приводится альтернативная функция
для определения чётности числа.
"""


def is_even(number: int) -> str | bool:
    """Функция получает на вход значение и пытается преобразовать
    его в int для проверки возможности проверки его на чётность"""
    if not isinstance(number, int):
        try:
            number = int(number)
        except (TypeError, ValueError):
            return f"Value {number} can't be converted"
    if number & 1:
        return False
    return True

