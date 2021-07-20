
y = ('+', '-', '*', '/')
flag = 1
res = 0


while True:
    nums = list(input('Введите через пробел 2 числа: ').split())
    sign = str(input('Введите через пробел  знак +, -, *, / для действий над числами. \nДля выхода введите 0: '))

    if sign == '0':
        break

    if sign not in y:
        sign = str(input('Вы ввели некооректный символ, попробуйте снова: '))

    if sign == y[0]:
        res = int(nums[0]) + int(nums[1])

    if sign == y[1]:
        res = int(nums[0]) - int(nums[1])

    if sign == y[2]:
        res = int(nums[0]) * int(nums[1])

    if sign == y[3]:
        if int(nums[1]) == 0:
            print('На 0 делить нельзя!\n')
            flag = 0
        else:
            res = int(nums[0]) / int(nums[1])

    if flag == 1:
        print(f'\nРезультат равен {res}\n')

    flag = 1

