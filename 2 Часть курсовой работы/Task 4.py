#имя файла: Task 4.py
#номер версии: 1.0
#автор и его учебная группа: Александровский А.П., ЭУ-142
#дата создания: 22.05.2019
#связанные файлы: пакет numpy
#версия Python: 3.6
#ОПИСАНИЕ:  Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
            # случайными элементами. Найти наименьшее значение среди средних
            # значений для каждой строки матрицы.



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
A = np.random.randint(0, 10, (N, M))
print(str(A) + "\n")

# Нахождение средних значений для каждой строки матрицы
Average = A.mean(axis=1)

# Нахождение номера строки с наибольшим средним значением
index = Average.argmin(axis=0)

# Нахождение наибольшее значение среди средних
# значений для каждой строки матрицы.
min = Average.min(axis=0)
print("Наименьшее значение среди средних значений: " + str(min))