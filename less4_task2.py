from time import time

#Поиск i-го простого числа без решета Эратосфена
z = int(input('Введите порядковый номер простого числа: '))

nums = [2]

def simple(n):
    num_s = 1
    if n == 1:
        return nums[-1]
    while num_s != n:
        x = nums[-1] + 1
        nums.append(x)
        count = 0
        for i in nums[1:-1]:
             if nums[-1] % i != 0:
                count += 1
                if count == len(nums[1:-1]):
                    num_s += 1
        if num_s == n:
            return nums[-1]

start_time = time()
print(f'Под индексом {z} находится простое число {simple(z)}')
end_time = time()

print(f'Время выполнения программы составило {end_time - start_time}')



"""z = int(input('Введите порядковый номер простого числа: '))
nums = []
res = []

for i in range(100000):
    nums.append(i)
    
start_time = time()

nums[1] = 0

curr_num = 2
while curr_num < nums[-1]:
    if nums[curr_num] != 0:
        curr_iter = curr_num * 2
        while curr_iter < nums[-1]:
            nums[curr_iter] = 0
            curr_iter += curr_num
    curr_num += 1


for i in nums:
    if nums[i] != 0:
        res.append(nums[i])

print(f'Под индексом {z} находится простое число {res[z-1]}')
end_time = time()

print(f'Время выполнения программы составило {end_time - start_time}')"""
