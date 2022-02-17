def count_zeros(n: int) -> int:
    if not isinstance(n, int): # != int:
        raise TypeError("Написано же: целое число вводить нужно...")
    if n < 0:
        raise ValueError("Введено отрицательное число. Не надо так...")
    res = 0
    while n > 0:
        n //= 5
        res += n
    return res


