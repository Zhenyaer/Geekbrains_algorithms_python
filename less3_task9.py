from random import randint

matrix = []
min_value = 0
min_values = []
max_value = 0


for i in range(5):
    matrix.append([])
    for j in range(10):
        nums = randint(1,100)
        matrix[i].append(nums)
print(matrix)

for j in range(len(matrix[0])):
    min_value = matrix[0][j]
    for i in range(len(matrix)):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
    min_values.append(min_value)

print(f'Минимальные элементы столбцов {min_values}')
max_value = min_values[0]

for i in range(len(min_values)):
    if min_values[i] > max_value:
        max_value = min_values[i]

print(f'Максимальный элемент среди минимальных элементов стобцов матрицы равен {max_value}')
