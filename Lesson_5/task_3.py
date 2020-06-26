my_dict = {}
with open('task_3_file.txt', encoding='utf-8') as file:
    for line in file:
        surname, salary = line.split()
        my_dict[surname] = salary
my_sum = 0
for key in my_dict:
    if float(my_dict[key]) < 20000:
        print(key)
    my_sum = my_sum + float(my_dict[key])

average = my_sum / len(my_dict)
print(f'Средний доход сотрудников: {average:.2f}')
