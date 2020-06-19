# Первый способ
def my_func(x, y):
    result = x ** y
    return result


answer = my_func(5, -2)
print(answer)


# Второй способ
def my_func_2(x, y):
    divider = 1
    for i in range(0, abs(y)):
        divider = divider * x
    result = 1 / divider
    return result


answer = my_func_2(2, -3)
print(answer)
