
x = 0

for i in range(32, 128):
    x += 1
    if x % 10 == 0:
        print(f'{i:4}: {chr(i)}')
    else:
        print(f'{i:4}: {chr(i)}', end=' ')
