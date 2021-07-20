n = int(input('Введите число n: '))

res = 1
x = 1

for i in range(1, n):
    x = x/2*(-1)
    res += x
    '''print(x)'''

print(f'Сумма элементов ряда равна {res}')
