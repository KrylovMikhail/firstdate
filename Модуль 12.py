

money = float(input('Введите сумму депозита: '))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit = [i * money / 100 for i in per_cent.values()]
print(deposit)
print('Максимальная сумма, которую вы можете заработать — ', max(deposit))















