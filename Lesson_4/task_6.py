from itertools import count, cycle

# а) итератор, генерирующий целые числа, начиная с указанного
num = int(input('Введите начальное число: '))
for i in count(start=num, step=1):
    print(i)
    if i >= num + 10:
        break

# б) итератор, повторяющий элементы некоторого списка, определенного заранее
my_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
i = 0
for color in cycle(my_list):
    print(color)
    i += 1
    if i >= 30:
        break
