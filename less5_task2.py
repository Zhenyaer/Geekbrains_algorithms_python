nums = [str(x) for x in range(10)]
nums += ['A', 'B', 'C', 'D', 'E', 'F']

first_num = [x for x in input('Введите первое число в 16-ричной система: ')]
second_num = [x for x in input('Введите второе число в 16-ричной система: ')]


def sum_16(x, y):
    res = ''
    k = 0

    while len(x) != len(y):
        if len(x) > len(y):
            y = ['0'] + y
        else:
            x = ['0'] + x

    x = ['0'] + x
    y = ['0'] + y


    for i in range(1, len(x) + 1):
        if nums.index(x[-i]) + nums.index(y[-i]) < len(nums):
            res = nums[nums.index(x[-i]) + nums.index(y[-i]) + k] + res
            k = 0
        else:
            res = nums[nums.index(x[-i]) + nums.index(y[-i]) + k - 16] + res
            k = 1

    if res[0] == '0':
        return res[1:]
    else:
        return res


def mul_16(x, y):
    x_10 = 0
    y_10 = 0
    res = ''

    for i in range(len(x)):
        x_10 += nums.index(x[-(i+1)]) * (16 ** i)

    for i in range(len(y)):
        y_10 += nums.index(y[-(i+1)]) * (16 ** i)

    res_10 = x_10 * y_10

    while res_10 != 0:
        a = res_10 % 16
        res_10 = res_10 // 16
        res = nums[a] + res

    return res


print(f'\nРезультат сложения введенных чисел равен: {sum_16(first_num, second_num)}')
print(f'Результат умножения введенных чисел равен: {mul_16(first_num, second_num)}')
