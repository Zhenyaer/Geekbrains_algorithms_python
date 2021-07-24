from random import randint

numbers = [randint(1,10) for x in range(20)]
print(f'Сгенерированный массив: {numbers}')

count = {int(x) : 0 for x in set(numbers)}

for i in numbers:
    count[i] += 1

mass = 0
mass_num = 0
mass_nums = []

for key in count:
    if count[key] > mass:
        mass = count[key]
        mass_num = key

for key in count:
    if count[key] == mass:
        mass_nums.append(str(key))

if len(mass_nums) > 1:
    print(f'Чаще всего встречаются числа {", ".join(mass_nums)}')
else:
    print(f'Чаще всего встречается число {mass_num}')
