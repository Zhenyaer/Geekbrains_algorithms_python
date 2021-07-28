from time import time

num = int(input('Введите число n: '))

def var1(n):
    res = 1
    x = 1
    for i in range(1, n):
        x = x/(-2)
        res += x
    return res

start_time1 = time()
res1 = var1(num)
end_time1 = time()

print(f'Сумма элементов ряда равна {res1}')
print(f'Время выполнения первого варианта составило {end_time1 - start_time1}')
# Сложность кода О(n)

def var2(n):
    res = 1
    x = 1
    for i in range(1, n):
        x = x * 2/(-2 * 2)
        res += x
    return res

start_time2 = time()
res2 = var2(num)
end_time2 = time()

print(f'Сумма элементов ряда равна {res2}')
print(f'Время выполнения второго варианта составило {end_time2 - start_time2}')
# Код выполняется чуть дольше
# Сложность кода О(n)

def var3(n):
    res = 1
    x = 1
    for i in range(1, n):
        x = (x - 0.5 * x) * (-1)
        res += x
    return res

start_time3 = time()
res3 = var3(num)
end_time3 = time()

print(f'Сумма элементов ряда равна {res3}')
print(f'Время выполнения третьего варианта составило {end_time3 - start_time3}')
# Код выполняется значительно дольше
# Сложность кода О(n)