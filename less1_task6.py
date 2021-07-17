user_input = int(input('Введите номер буквы латинского алфавита: '))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(f'Под номером {user_input} находится буква {alphabet[user_input-1].upper()}')