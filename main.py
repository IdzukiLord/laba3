# main.py

def plus(a, b):
    """Функция сложения.

    Args:
        a (int): Первый операнд.
        b (int): Второй операнд.

    Returns:
        int: Результат сложения a и b.
    """
    return a + b

def minus(a, b):
    """Функция вычитания.

    Args:
        a (int): Уменьшаемое.
        b (int): Вычитаемое.

    Returns:
        int: Результат вычитания b из a.
    """
    return a - b

if __name__ == "__main__":
    print("Сложение:", plus(2, 3))
    print("Вычитание:", minus(5, 3))
