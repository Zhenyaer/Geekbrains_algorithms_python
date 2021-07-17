user_input = list(input('Введите три разные числа через пробел: ').split())

if len(user_input) != 3:
    print(f'Введенное вами число не трехзначное!')
else:
    x = int (user_input[0])
    y = int(user_input[1])
    z = int (user_input[2])
    if x != y and x != z:
        if ((x > y) and (x < z)) or ((x > z) and (x < y)):
            print(f'\nСреднее число {x}')
        elif ((y > x) and (y < z)) or ((y > z) and (y < z)):
            print(f'\nСреднее число {y}')
        else:
            print(f'\nСреднее число {z}')
    else:
        print(f'Среди введенных чисел есть одинаковые!')
