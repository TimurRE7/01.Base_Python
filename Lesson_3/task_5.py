def my_sum(numbers):
    numbers_list = numbers.split()
    result = 0
    stop = False
    for i in range(len(numbers_list)):
        try:
            result = result + int(numbers_list[i])
        except ValueError:
            stop = True
            break
    return result, stop


print('Для выхода введите любую букву')
answer = 0
while True:
    user_numbers = input('Введите числа через пробел: ')
    answer = answer + my_sum(user_numbers)[0]
    print(f'Сумма равна {answer}')
    if my_sum(user_numbers)[1]:
        break
