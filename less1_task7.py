user_input = list(input('Введите длины сторон треугольника через пробел: ').split())

if len(user_input) != 3:
    print(f'В треугольнике 3 стороны!')
else:
    a = int (user_input[0])
    b = int(user_input[1])
    c = int (user_input[2])
    if (a > b + c) or (b > a + c) or c > (a + b):
        print('Треугольник не существует!')
    else:
        if a == b and b == c:
            print('Треугольник равносторонний')
        elif a == b or b == c or a == c:
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')
