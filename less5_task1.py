num_fact = int(input('Введите количество предприятий: '))
factories = {}
sum_profit = 0

for i in range(num_fact):
    sum_prof = 0
    name = input(f'Введите наименование {i+1}-го предприятия: ')
    profit = [int(input(f'Введите прибыль предприятия {name} за {x+1} квартал: ')) for x in range(4)]
    factories.update({name: profit})
    for j in profit:
        sum_prof += j
    sum_profit += sum_prof

avg_profit = sum_profit / num_fact
print(f'\nСредняя годовая прибыль предприятий составляет {avg_profit}')

print('\nСписок предприятий с прибылью выше или равной средней: ')
for key, value in factories.items():
    sum_prof = 0
    for j in value:
        sum_prof += j4
    if sum_prof >= avg_profit:
        print(f'{key}: {sum_prof}')


print('\nСписок предприятий с прибылью ниже средней: ')
for key, value in factories.items():
    sum_prof = 0
    for j in value:
        sum_prof += j
    if sum_prof < avg_profit:
        print(f'{key}: {sum_prof}')
