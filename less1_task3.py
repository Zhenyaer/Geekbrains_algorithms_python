import math
A = list(input('Введите координаты первой точки через пробел (x1 y1): ').split())
B = list(input('Введите координаты второй точки через пробел (x2 y2): ').split())

x1 = float(A[0])
y1 = float(A[1])
x2 = float(B[0])
y2 = float(B[1])

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

if b > 0:
    print(f'\nУравнение прямой: y = {k}x + {b}')
else:
    print(f'\nУравнение прямой: y = {k}x - {math.fabs(b)}')
