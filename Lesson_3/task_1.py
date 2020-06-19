def divide():
    number_1 = int(input('Введите делимое: '))
    number_2 = int(input('Введите делитель: '))
    try:
        result = number_1 / number_2
        print(f'Результат: {result:.2f}')
    except ZeroDivisionError:
        print('На ноль делить нельзя')


divide()
