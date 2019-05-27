#имя файла: Task 11.py
#номер версии: 1.0
#автор и его учебная группа: Александровский А.П., ЭУ-142
#дата создания: 22.05.2019
#связанные файлы: пакет numpy
#версия Python: 3.6
#ОПИСАНИЕ:  Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
            #случайными элементами. Просуммировать элементы каждой строки
            #матрицы с соответствующими элементами L-й строки.




# Подключение библиотеки Numpy и Random
import numpy as np
import random

# Число строк и столбцов
N = random.randint(2, 10)
M = random.randint(2, 10)

# К-ый столбец матрицы
L = random.randint(1, N-1)

# Так как матрица должна быть прямоугольной, то N не может быть равно M
while N == M:
    N = random.randint(2, 10)
    M = random.randint(2, 10)

# Создание матрицы
A = np.random.randint(0, 10, (N, M))
print(str(A) + "\n")

# Определение L строки
L_arr = np.array(A[L-1, :])
print("L страка: \n" + str(L_arr))

# Сложение элеменотов
A = A + L_arr

print("\nНовая матрица: \n" + str(A))