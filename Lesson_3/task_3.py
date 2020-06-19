def my_func(arg_1, arg_2, arg_3):
    delta = min(arg_1, arg_2, arg_3)
    answer = arg_1 + arg_2 + arg_3 - delta
    return answer


result = my_func(10, 25, 44)
print(result)
