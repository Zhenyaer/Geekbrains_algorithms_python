matrix = []
sum_str = 0

for i in range(4):
    matrix.append([])
    for j in range(4):
        user_input = int(input(f'Введите элемент {i+1} строки и {j+1} столбца: '))
        sum_str += user_input
        matrix[i].append(user_input)
    matrix[i].append(sum_str)
    
for x in matrix:
    print(('{:4d}' * 5).format(*x))