import pytest
from task1.solution.main import sum_two


def test_sum_two_with_str_arg():
    """Проверяет, что передача строки вместо числа вызывает TypeError."""
    with pytest.raises(TypeError) as excinfo:
        sum_two(1, "2")
    assert "Аргумент 'b' должен быть int, а не str" in str(excinfo.value)


def test_sum_two_with_float_first_arg():
    """Проверяет, что передача float вместо int вызывает TypeError."""
    with pytest.raises(TypeError) as excinfo:
        sum_two(1.0, 1)
    assert "Аргумент 'a' должен быть int, а не float" in str(excinfo.value)


def test_sum_two_with_float_second_arg():
    """Проверяет, что передача float вместо int вызывает TypeError."""
    with pytest.raises(TypeError) as excinfo:
        sum_two(1, 123.91)
    assert "Аргумент 'b' должен быть int, а не float" in str(excinfo.value)


def test_sum_two_with_bool_arg():
    """Проверяет, что передача bool вместо int вызывает TypeError."""
    with pytest.raises(TypeError) as excinfo:
        sum_two(1, True)
    assert "Аргумент 'b' должен быть int, а не bool" in str(excinfo.value)