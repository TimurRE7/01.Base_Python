user_string = input('Введите строку: ')
my_list = user_string.split()
i = 1
for word in my_list:
    print(f'{i}: {word[:10]}')
    i += 1
