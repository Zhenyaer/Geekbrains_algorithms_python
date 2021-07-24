from random import randint

numbers = [randint(-100,100) for x in range(20)]
print(f'Сгенерированный массив: {numbers}')

max_neg = 0
ind = 0
n = 0

for i in numbers:
    if i < 0:
        max_neg = i
        break

for i in numbers:
    if i < 0:
        if i > max_neg:
            max_neg = i
            ind = n
    n += 1

if max_neg < 0:
    print(f'Самый максимальный отрицательный элемент массива {max_neg} c индексом {ind}')
else:
    print('В сгенерированном массиве нет отрицательных элементов')
