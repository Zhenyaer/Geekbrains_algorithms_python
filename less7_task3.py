from random import randint

num = int(input('Введите натуральное число: '))
massive = [randint(0,1000) for x in range(2 * num + 1)]

print(f'Исходный массив:\n{massive}')

for i in massive:
    less_el = 0
    more_el = 0
    for j in massive:
        if i < j:
            less_el += 1
        elif i > j:
            more_el += 1
    if less_el == more_el:
        print(f'Медианный элемент массива: {i}')
        break

