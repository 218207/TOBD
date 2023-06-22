import dask.dataframe as dd

# Читаем все файлы в директории, которые соответствуют шаблону
accounts = dd.read_csv("accounts.*.csv",
                       dtype={"amount": "float64", "id": "int64", "names": "object"})

# Отфильтровываем данные, оставляя только значения, кратные трем
multiples_of_three = accounts[accounts.amount % 3 == 0]

# Группируем данные по ID и считаем количество таких значений
grouped = multiples_of_three.groupby('id').size()

# Ищем ID с наибольшим количеством значений, кратных трем
result_id = grouped.idxmax().compute()

print(f"id, для которого в столбце amount встречается наибольшее количество значений, кратных трем {result_id}")

