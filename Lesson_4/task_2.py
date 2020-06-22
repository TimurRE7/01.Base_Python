task_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [task_list[i] for i in range(1, len(task_list)) if task_list[i] > task_list[i-1]]
print(result_list)
