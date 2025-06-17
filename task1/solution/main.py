def strict(func):
    """Декоратор для проверки типов аргументов функции.

    Проверяет, что типы переданных аргументов соответствуют аннотациям функции.
    При несоответствии типов вызывает исключение TypeError.

    Args:
        func: Декорируемая функция с аннотациями типов

    Returns:
        Обёрнутая функция с проверкой типов
    """
    def wrapper(*args, **kwargs):
        for name, value in func.__code__.co_varnames, args:
            if name in func.__annotations__:
                expected = func.__annotations__[name]
                if (type(value) is bool and expected is int) or type(value) is not expected:
                    raise TypeError(
                        f"Аргумент '{name}' должен быть {expected.__name__}, а не {type(value).__name__}"
                    )
        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# print(sum_two(1, 2))  # 3
# print(sum_two(1, "2"))  # TypeError: Аргумент 'b' должен быть int, а не str
# print( sum_two(1, False)) # TypeError: Аргумент 'b' должен быть int, а не bool

