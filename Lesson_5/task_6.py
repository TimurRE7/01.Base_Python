my_dict = {}
with open('task_6_file.txt', encoding='utf-8') as file:
    text = file.readlines()
    print(text)
    for line in text:
        string = line.split()
        print(string)
        summa = 0
        for _ in line[1:]:
            num = _.split('(')
            print(num)
            try:
                summa = summa + int(num[0])
            except ValueError:
                pass
        print(summa)