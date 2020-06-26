my_file = open('task_1_file.txt', 'w')
stop = True
while stop:
    my_string = input('Введите данные: ')
    my_file.write(my_string + '\n')
    if my_string == '':
        stop = False
my_file.close()
