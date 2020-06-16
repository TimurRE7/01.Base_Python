my_list = [7, 5, 3, 3, 2]
my_list2 = [7, 5, 3, 3, 2]
number = int(input('Введите номер рейтинга: '))

# Решение 1
if number > my_list[0]:
    my_list.insert(0, number)
elif number <= my_list[-1]:
    my_list.append(number)
else:
    for i in range(0, len(my_list)):
        if number <= my_list[i]:
            continue
        else:
            my_list.insert(i, number)
            break
print(f'Пользователь ввел число: {number}. Результат: {my_list}')

# Решение 2
my_list2.append(number)
my_list2.sort(reverse=True)
print(f'Пользователь ввел число: {number}. Результат: {my_list}')
