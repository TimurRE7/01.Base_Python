import random

line = ''
with open('task_5_file.txt', 'w') as file:
    for _ in range(10):
        number = random.randint(0, 20)
        line = line + str(number) + ' '
    file.write(line)

result = 0
with open('task_5_file.txt') as file:
    line = file.readline()
    numbers = line.split()
    for number in numbers:
        result = result + int(number)
    print(result)