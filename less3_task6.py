from random import randint

numbers = [randint(1,100) for x in range(20)]
print(f'Сгенерированный массив: {numbers}')

sum_min_max = 0
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

if min_ind < max_ind:
    for i in numbers[min_ind + 1:max_ind]:
        sum_min_max += i
else:
    for i in numbers[max_ind + 1:min_ind]:
        sum_min_max += i

print(f'Сумма элементов между максимальным и минимальным равна: {sum_min_max}')
