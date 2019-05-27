#имя файла: Task 5.py
#номер версии: 1.0
#автор и его учебная группа: Александровский А.П., ЭУ-142
#дата создания: 22.05.2019
#связанные файлы: пакет numpy
#версия Python: 3.6
#ОПИСАНИЕ:  Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
            #случайными элементами. Определить средние значения по всем строкам и
            #столбцам матрицы. Результат оформить в виде матрицы из N + 1 строк и M
            #+ 1 столбцов.



# Подключение библиотеки Numpy и Random
import numpy as np
import random

# Число строк и столбцов
N = random.randint(2, 10)
M = random.randint(1, 10)

# Так как матрица должна быть прямоугольной, то N не может быть равно M
while N == M:
    N = random.randint(1, 10)
    M = random.randint(1, 10)

# Создание матрицы
A = np.random.randint(0, 10, (N, M)).astype(np.float64)
print(str(A) + "\n")

# Нахождение средних значений для каждой строки и столбца матрицы
Average_line = A.mean(axis=1)
Average_column = A.mean(axis=0)

# Добавление столбца и строки к матрице A
Average_line = Average_line[: , np.newaxis]
A = np.hstack((A, Average_line))

Average_column = np.hstack((Average_column, [0.]))
A = np.vstack((A, Average_column))

print("\nНовая матрица: \n" + str(A))