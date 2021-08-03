# Разрядность ОС Х64
# Версия python 3.8.5

# Lesson3_task1
l = [int(x) for x in range(2,100)]
nums = [int(x) for x in range(2,10)]

for i in nums:
    a = 0
    for j in l:
        if j % i == 0:
            a += 1
    print(f'В диапазоне от 2 до 99 {a} чисел кратных {i}')

# Переменная l занимает 40 + 8*98 + 24*98 = 3176 б = 3,1 Kб
# Переменная nums занимает 40 + 8*8 + 24*8 = 296 б


# Lesson3_task2
from random import randint

numbers = [randint(1,100) for x in range(10)]
print(f'Сгенерированный список: {numbers}')
ind = []
n = 0

for i in numbers:
    if i % 2 == 0:
        ind.append(n)
    n += 1

print(f'В сгенерированном списке индексы четных элементов равны: {ind}')

# Переменная numbers занимает 40 + 8*10 + 24*10 = 360 б


# Lesson1_task6
user_input = int(input('Введите номер буквы латинского алфавита: '))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(f'Под номером {user_input} находится буква {alphabet[user_input-1].upper()}')

# Переменная alphabet занимает 40 + 8*26 + 26*(37 + 1) = 1236 б

## Первые 2 варианта оптимальнее с точки зрения использования памяти так как строковый тип данных занимает больше места чем целочисленный