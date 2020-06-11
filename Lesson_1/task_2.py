user_time = int(input('Введите время в секундах: '))

hours = user_time // 3600
minutes = (user_time - 3600 * hours) // 60
seconds = user_time - ((hours * 3600) + (minutes * 60))

if hours < 10:
    hours = '0' + str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)

print(f'Время {hours}:{minutes}:{seconds}')