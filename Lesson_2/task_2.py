user_list = []
number = int(input('Введите количество элементов списка: '))
for _ in range(number):
    user_list.append(input('Введите элемент списка: '))
print('Введенный список:', user_list)
for i in range(1, number, 2):
    user_list[i], user_list[i-1] = user_list[i-1], user_list[i]
print('Полученный список:', user_list)
