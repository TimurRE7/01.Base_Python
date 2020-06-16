number = int(input('Введите количество товаров: '))

product_list = []
product_dict = {'название': '', 'цена': 0, 'количество': 0, 'eд.': ''}
analysis_dict = {}

for i in range(number):
    product_dict = product_dict.copy()
    for key in product_dict:
        value = input(f'Введите {key} ')
        try:
            product_dict[key] = int(value)
        except ValueError:
            product_dict[key] = value
    product_list.append((i+1, product_dict))

print('')  # Отступ

for _ in range(len(product_list)):
    print(product_list[_])

print('')  # Отступ

for key in product_dict:
    analysis_list = []
    for i in range(number):
        analysis_list.append(product_list[i][1][key])
    analysis_dict[key] = analysis_list

for key in analysis_dict:
    print(f'{key}: {analysis_dict[key]}')
