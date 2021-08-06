from random import randint

massive = [randint(-100,100) for x in range(20)]
print(f'Исходный массив:\n{massive}')

def sort(m):
    for i in range(len(m)):
        for j in range(len(m) - i - 1):
            if m[j] < m[j+1]:
                m[j], m[j+1] = m[j+1], m[j]
    return m

print(f'\nОтсортированный массив:\n{sort(massive)}')

