user_input = str(input('Введите любое число: '))

res= ''

for i in range(len(user_input)):
    res = user_input[i] + res

print(f'Обратное число равно {res}')