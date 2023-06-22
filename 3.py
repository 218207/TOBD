import dask.array as da
import h5py

# Открываем файл hdf5 с помощью h5py
file = h5py.File('rnd_data.hdf5', 'r')

# Читаем данные из файла в Dask массив
data = da.from_array(file['data_set_1'], chunks='auto')

# Вычисляем среднее значение и стандартное отклонение
mean = data.mean()
std = data.std()

# Определяем пороговое значение
threshold = mean + 3 * std

# Фильтруем значения, превышающие порог
filtered_data = data[data > threshold]

# Вычисляем долю значений, превышающих порог
fraction = filtered_data.size / data.size

# Выводим результат
print("Доля значений, превышающих среднее значение более чем на 3 стандартных отклонения:", fraction)

# Закрываем файл
file.close()

# Открываем файл hdf5 с помощью h5py
file = h5py.File('rnd_data.hdf5', 'r')

# Выводим список ключей в файле
print(list(file.keys()))

# Закрываем файл
file.close()


