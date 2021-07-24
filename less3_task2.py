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
