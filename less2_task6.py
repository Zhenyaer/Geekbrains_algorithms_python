from random import randint

print('Отгадайте загаданное число от 0 до 100 за 10 попыток')

x = randint(0,100)
n = 0
while n < 10:
    n += 1
    user_input = int(input('\nВведите число: '))
    if user_input > x:
        print(f'Попытка #{n} \nВы ввели большее число!')
    elif user_input < x:
        print(f'Попытка #{n} \nВы ввели меньшее число!')
    else:
        print(f'Попытка #{n} \n\nПоздравляем! Вы отгадали число {x}')
        break

if n == 10:
    print(f'\n\nВы исчерпали попытки! Было загадано число {x}')
