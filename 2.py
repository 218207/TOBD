import pandas as pd

# Загрузка данных из файла в DataFrame
df = pd.read_csv('sp500hst.txt', delimiter=',', header=None, names=['date', 'ticker', 'open', 'high', 'low', 'close', 'volume'])

# Фильтрация данных для тикера NVDA
nvda_df = df[df['ticker'] == 'NVDA']

# Нахождение минимального и максимального значения цены открытия
min_open_price = nvda_df['open'].min()
max_open_price = nvda_df['open'].max()

# Фильтрация данных для периода между минимальным и максимальным значениями цены открытия
period_df = nvda_df[(nvda_df['open'] == min_open_price) | (nvda_df['open'] == max_open_price)]

# Нахождение количества дней между минимальным и максимальным значениями цены открытия
days_passed = len(period_df)

# Вычисление суммарного объема торгов за период
total_volume = period_df['volume'].sum()

# Вывод результатов
print("Количество дней между минимальной и максимальной ценой открытия:", days_passed)
print("Суммарный объем торгов:", total_volume)