from random import randint, uniform

user_input = list(input('Введите границы диапазона (целочисленные, вещественные или буквенные латинского алфавита) через пробел: ').split())

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

try:
    a = int(user_input[0])
    b = int(user_input[1])
    res = randint(a,b)
    print(f'Случайное число из введенного диапазона равно {res}')
except ValueError:
    try:
        a = float(user_input[0])
        b = float(user_input[1])
        res = uniform(a, b)
        print(f'Случайное число из введенного диапазона равно {res}')
    except ValueError:
        try:
            a = alphabet.index(user_input[0])
            b = alphabet.index(user_input[1])
            res = alphabet[randint(a,b)]
            print(f'Случайная буква внутри введенного диапазона равна {res.title()}')
        except ValueError:
            print('Вы ввели неверные данные')
