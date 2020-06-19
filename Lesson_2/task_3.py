user_month = int(input('Введите месяц в виде целого числа от 1 до 12: '))

# Решение через list

month_list = ['зима', 'весна', 'лето', 'осень']

if 2 < user_month < 6:
    season = 1
elif 5 < user_month < 9:
    season = 2
elif 8 < user_month < 12:
    season = 3
else:
    season = 0

print('Время года:', month_list[season])

# Решение через dict

month_dict = {'Зима': (1, 2, 12), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}

for key in month_dict:
    if user_month in month_dict[key]:
        print('Время года:', key)
