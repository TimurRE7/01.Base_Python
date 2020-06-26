import json

my_dict = {}
summary_profit = 0
i = 0
with open('task_7_file.txt', encoding='utf-8') as file:
    task_list = file.readlines()
    for line in task_list:
        string = line.split()
        if string[2] > string[3]:
            summary_profit = summary_profit + int(string[2]) - int(string[3])
            i +=1
        my_dict[string[0]] = int(string[2]) - int(string[3])

average_profit = summary_profit / i
profit_dict = {'average_profit': average_profit}
my_list = [my_dict, profit_dict]

print(my_dict)
print(my_list)

with open('task_7.json', 'w') as f_json:
    json.dump(my_list, f_json)
