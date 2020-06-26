with open('task_4_file.txt', encoding='utf-8') as task:
    with open('task_4_file_done.txt', 'w') as done:
        for line in task:
            if line.split()[0] == 'One':
                new_line = line.replace('One', 'Один')
            elif line.split()[0] == 'Two':
                new_line = line.replace('Two', 'Два')
            elif line.split()[0] == 'Three':
                new_line = line.replace('Three', 'Три')
            elif line.split()[0] == 'Four':
                new_line = line.replace('Four', 'Четыре')
            done.write(new_line)
