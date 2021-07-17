import math

user_input = list(input('Введите две буквы латинского алфавита через пробел: ').split())

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

quantity = int(math.fabs(alphabet.index(user_input[0]) - alphabet.index(user_input[1])))

print(f'\nБуква {user_input[0]} находится на {alphabet.index(user_input[0]) + 1} месте')
print(f'Буква {user_input[1]} находится на {alphabet.index(user_input[1]) + 1} месте')
print(f'Между введенными буквами находится {quantity} букв')