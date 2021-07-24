from random import randint

numbers = [randint(1,100) for x in range(20)]
print(f'Сгенерированный массив: {numbers}')

min_1 = numbers[0]
min_1_ind = 0
min_2 = numbers[0]
min_2_ind = 0
n = 0

for i in numbers:
    if i < min_1:
        min_1 = i
        min_1_ind = n
    n += 1

n = 0

for i in numbers:
    if i < min_2 and n != min_1_ind:
        min_2 = i
        min_2_ind = n
    n += 1

print(f'Наименьшие 2 числа в массиве равны {min_1} и {min_2}')
