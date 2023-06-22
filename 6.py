import dask.dataframe as dd

# Читаем все файлы в директории, которые соответствуют шаблону
accounts = dd.read_csv("accounts.*.csv",
                       dtype={"amount": "float64", "id": "int64", "names": "object"})

# Отфильтровываем данные, оставляя только положительные значения
positive_amounts = accounts[accounts.amount > 0]

# Группируем данные по ID и суммируем amount
grouped = positive_amounts.groupby('id').amount.sum()

# Ищем ID с наибольшей суммой
result_id = grouped.idxmax().compute()

print(f" ID с наибольшей суммой положительных значений в столбце amount {result_id}")
