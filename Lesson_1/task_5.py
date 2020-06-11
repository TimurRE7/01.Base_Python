revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

profit = revenue - costs

if profit > 0:
    print('Прибыль составила', profit)
    number_staff = int(input('Введите численность сотрудников: '))
    print('Прибыль на одного сотрудника составила', profit / number_staff)
else:
    print('Убыток составил', 0 - profit)

# В задании сказано определить прибыль на сотрудника, поэтому убыток не считал
