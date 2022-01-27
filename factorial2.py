def func():
    n = int(float(input('Введи положительное целое число, брат: ')))
    res = 0
    while n > 0:
        n //= 5
        res += n
    # print(res, ' нулей в конце факториала')
    return res

print(func(), ' нулей в конце факториала, брат')
