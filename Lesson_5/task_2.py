my_file = open('task_2_file.txt')

lines = my_file.readlines()
row_number = len(lines)
print('Строк:', row_number)
for i, row in enumerate(lines):
    words = len(row.split())
    print(f'Слов в строке {i + 1}: {words}')
