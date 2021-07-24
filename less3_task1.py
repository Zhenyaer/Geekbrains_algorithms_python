l = [int(x) for x in range(2,100)]
nums = [int(x) for x in range(2,10)]

for i in nums:
    a = 0
    for j in l:
        if j % i == 0:
            a += 1
    print(f'В диапазоне от 2 до 99 {a} чисел кратных {i}')
