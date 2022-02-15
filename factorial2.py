userInput = input('Введите целое положительное число: ')   # userInput - строковая пер-ная для ввода числа;
def count_zeros(n: str) -> str:     # объявили функ-ю согласно замечанию;
    if not n.isdigit():   # проверили на целостность введёное значение - isdigit вообще тема!
        return 'TypeError: введеное значение не является целым числом.'
    elif int(n) < 0:    # проверили на отрицательное число преобразовав в тип int
        return 'ValueError: введено отрицательное число. Не надо так.'
    else:   # основное тело функции
        int_variable = int(n)
        res = 0
        while int_variable > 0:
            int_variable //= 5
            res += int_variable
        return str(res) + ' нулей в конце факториала'   # сделали res строкой -выполнили условие объявления функ-ии
print(count_zeros(userInput))
