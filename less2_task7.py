num = int(input('Введите натуральное число: '))

res1 = 0
res2 = 0

for i in range(num):
    res1 += i

res2 = num * (num + 1) / 2

if res1 == res2:
    print('Равенство 1+2+...+n = n(n+1)/2 верно')
else:
    print('Равенство 1+2+...+n = n(n+1)/2 не верно')
