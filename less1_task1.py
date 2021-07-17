
user_input = list(input('Введите целое трехзначное число: '))


if len(user_input) != 3:
    print(f'Введенное вами число не трехзначное!')
else:
    summa = 0
    umn = 1
    for i in range(len(user_input)):
        summa += int(user_input[i-1])
    for i in range(len(user_input)):
        umn *= int(user_input[i-1])
    print(f'\nСумма цифр введенного числа равна {summa}')
    print(f'Произведение цифр введенного числа равно {umn}')
