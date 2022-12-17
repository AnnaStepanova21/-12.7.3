per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Ввести сумму вклада: '))
deposit = [money*per_cent/100 for per_cent in per_cent.values()]
max_deposit = max(deposit)
print(deposit)
print("Максимальная сумма, которую вы можете заработать " + str(max_deposit))
