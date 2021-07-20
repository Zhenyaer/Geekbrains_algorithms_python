user_input = str(input('Введите любое целое число: '))

a = 0
b = 0
for i in range(len(user_input)):
    if int(user_input[i]) % 2 == 0:
        a += int(user_input[i])
    else:
        b += int(user_input[i])

print(f'Сумма четных цифр равна: {a}')
print(f'Сумма нечетных цифр равна: {b}')
