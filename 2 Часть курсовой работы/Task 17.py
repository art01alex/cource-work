#имя файла: Task 17.py
#номер версии: 1.0
#автор и его учебная группа: Александровский А.П., ЭУ-142
#дата создания: 22.05.2019
#связанные файлы: пакет numpy
#версия Python: 3.6
#ОПИСАНИЕ:  Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
            #случайными элементами. Добавить к матрице строку и вставить ее под
            #номером L.




# Подключение библиотеки Numpy и Random
import numpy as np
import random

# Число строк и столбцов, число L
N = random.randint(2, 10)
M = random.randint(1, 10)
L = random.randint(1, N)

# Так как матрица должна быть прямоугольной, то N не может быть равно M
while N == M:
    N = random.randint(1, 10)
    M = random.randint(1, 10)

# Создание матрицы
A = np.random.randint(0, 10, (N, M))
print(str(A) + "\n")

# Создание дополнительной строки
a = np.random.randint(0, 10, M)
print("Допонлительная строка: " + str(a))

# Добавление строки под номером L
print("\n L = " + str(L))

if L == N:
    X = np.vstack((A, a))
elif L != N:
    X = np.array(A[0, :])
    for i in range (1, N):
        if i == L:
            X = np.vstack((X, a))
            X = np.vstack((X, A[i, :]))
        elif i  != L:
            X = np.vstack((X, A[i, :]))
print("\nНовая матрица: \n" + str(X))