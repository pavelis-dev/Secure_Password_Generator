import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
flag = False
password = ''


def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password


while True:
    count_password = input('Введите количество паролей, которое необходимо сгенерировать: ')
    if count_password.isdigit() and int(count_password) >= 1:
        count_password = int(count_password)
        break
    else:
        print('Введите целое число от 1 и выше!')

while True:
    length = input('Введите длинну паролей: ')
    if length.isdigit() and int(length) >= 8:
        length = int(length)
        break
    else:
        print('Введите целое число от 8 и выше!')

print('Включать цифры?')
a = input('Введите: "1" - вкючить, "enter" - нет ')
print('Включать прописные буквы?')
b = input('Введите: "1" - вкючить, "enter" - нет ')
print('Включать строчные буквы?')
c = input('Введите: "1" - вкючить, "enter" - нет ')
print('Включать символы?')
d = input('Введите: "1" - вкючить, "enter" - нет ')
print('Исключать неоднозначные символы il1Lo0O ?')
e = input('Введите: "1" - исключить, "enter" - нет ')

if a == '1':
    chars += digits
if b == '1':
    chars += lowercase_letters
if c == '1':
    chars += uppercase_letters
if d == '1':
    chars += punctuation
if e == '1':
    for c in 'il1Lo0':
        chars = chars.replace(c, '')

for _ in range(count_password):
    print(generate_password(length, chars))
