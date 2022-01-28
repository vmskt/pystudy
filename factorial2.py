b = int(float(input('Введи положительное целое число, брат: ')))
def func(n):
    res = 0
    while n > 0:
        n //= 5
        res += n
    return res
print(func(b), ' нулей в конце факториала, брат')
