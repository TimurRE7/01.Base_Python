user_number = input('Введите целое положительное число: ')

max = 0
i = 0

while i < len(user_number):
    if max < int(user_number[i]):
        max = int(user_number[i])
    i += 1

print(max)