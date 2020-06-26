my_dict = {}
with open('task_6_file.txt', encoding='utf-8') as file:
    text = file.readlines()
    for line in text:
        string = line.split()
        summa = 0
        for _ in string[1:]:
            num = _.split('(')
            try:
                summa = summa + int(num[0])
            except ValueError:
                pass
        my_dict[string[0]] = summa
print(my_dict)