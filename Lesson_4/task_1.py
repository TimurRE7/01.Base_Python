import sys
import time

args = sys.argv[1:]
if 'help' in args:
    print('Введите через пробел: выработку, ставку, премию')
elif args[0].isdigit() and args[1].isdigit() and args[2].isdigit():
    print('Идет подсчет')
    time.sleep(1)
    result = int(args[0]) * int(args[1]) + int(args[2])
    print(f'Заработная плата сотрудника: {result}')
else:
    print('Ошибка')
