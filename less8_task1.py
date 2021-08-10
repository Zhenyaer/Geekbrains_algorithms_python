from random import randint
import hashlib


user_input = int(input('Введите длину строки: '))

alphabet = ['a', 'b' ,'c', 'd', 'e', 'f', 'g', 'h' ,'i', 'j', 'k', 'l', 'm', 'n' ,'o', 'p', 'q', 'r', 's', 't' ,'u', 'v', 'w', 'x', 'y', 'z']
s = ''
h = []

for i in range(user_input):
    s += alphabet[randint(0, len(alphabet) - 1)]
print(f'Сгенерирована строка {s}')

for i in range(len(s) + 1):
    for j in range(i + 1, len(s) + 1):
        a = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
        h.append(a)

print(f'Количество различных подстрок в строке {s} равно: {len(h)}')
