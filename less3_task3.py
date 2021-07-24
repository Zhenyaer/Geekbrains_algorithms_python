from random import randint

numbers = [randint(1,100) for x in range(20)]
print(f'Сгенерированный массив: {numbers}')

min_el = numbers[0]
max_el = numbers[0]
min_ind = 0
max_ind = 0
n = 0

for i in numbers:
    if i < min_el:
        min_el = i
        min_ind = n
    if i > max_el:
        max_el = i
        max_ind = n
    n += 1

print(f'Минимальный элемент: {min_el} c индексом {min_ind}')
print(f'Максимальный элемент: {max_el} c индексом {max_ind}')

numbers[min_ind], numbers[max_ind] = numbers[max_ind], numbers[min_ind]

print(f'Измененный массив:      {numbers}')
