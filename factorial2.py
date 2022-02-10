userInput = int(input('Введи положительное целое число, брат: '))
def count_zeros(n):
    res = 0
    while n > 0:
        n //= 5
        res += n
    return res
print(count_zeros(userInput), ' нулей в конце факториала, брат')
