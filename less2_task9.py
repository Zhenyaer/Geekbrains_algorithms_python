user_input = list(input('Введите любые натуральные числа через пробел: ').split())

sum_1 = 0
sum_max = 0
num_max = 0


for i in range(len(user_input)):
    for j in range(len(user_input[i])):
        sum_1 += int(user_input[i][j])
    if sum_1 > sum_max:
        sum_max = sum_1
        num_max = user_input[i]
        sum_1 = 0
    else:
        sum_1 = 0

print(f'\nНаибольшая сумма цифр числа равна: {sum_max}')
print(f'Это число равно: {num_max}')
