import numpy as np

A = np.array([[8,4,15,6,9],[3,16,13,8,10],[0,9,18,17,5],[16,2,6,0,10],[18,13,9,17,8]])

# находим минимальный элемент по строкам и столбцам
min_rows = np.min(A, axis=1)
min_cols = np.min(A, axis=0)

# создаем массив В
B = min_rows.reshape(-1, 1) + min_cols.reshape(1, -1)

print(B)
