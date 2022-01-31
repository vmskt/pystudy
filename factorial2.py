userInput = int(input('Введи положительное целое число, брат: '))
def func(n):
    res = 0
    while n > 0:
        n //= 5
        res += n
    return res
print(func(userInput), ' нулей в конце факториала, брат')
