def count_zeros(n: int) -> int:
    """Данная функция возвращает количество нулей в конце факториала от введённого числа."""
    if not isinstance(n, int): # != int:
        raise TypeError("Написано же: целое число вводить нужно...")
    if n < 0:
        raise ValueError("Введено отрицательное число. Не надо так...")
    res = 0
    while n > 0:
        n //= 5
        res += n
    return res

if __name__ == '__main__':
    positive_input = {0:0, 1:0, 5:1, 9:1, 10:2, 14:2, 15:3, 19:3, 20:4, 25:6, 30:7}
    for key, value in positive_input.items():
        print(f'{key}:{value}')
        assert count_zeros(key) == value
