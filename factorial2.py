def func():
    n = int(float(input('Введи положительное целое число, брат: ')))
    res = 0
    while n > 0:
        n //= 5
        res += n
    return res

print(func(), ' нулей в конце факториала, брат')
