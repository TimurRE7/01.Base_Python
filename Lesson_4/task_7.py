from math import factorial
from itertools import count


def fact():
    for i in count(start=1, step=1):
        yield i, factorial(i)


n = int(input('Введите число: '))

for num, el in fact():
    print(f'{num}!={el}')
    if num >= n:
        break
