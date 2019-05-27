#имя файла: Task 29.py
#номер версии: 1.0
#автор и его учебная группа: Александровский А.П., ЭУ-142
#дата создания: 22.05.2019
#связанные файлы: пакет numpy
#версия Python: 3.6
#ОПИСАНИЕ:  Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
            #случайными элементами. Добавить к матрице столбец чисел и вставить его
            #под номером K.




# Подключение библиотеки Numpy и Random
import numpy as np
import random

# Число строк и столбцов, число L
N = random.randint(2, 10)
M = random.randint(2, 10)
K = random.randint(1, M)

# Так как матрица должна быть прямоугольной, то N не может быть равно M
while N == M:
    N = random.randint(1, 10)
    M = random.randint(1, 10)

# Создание матрицы
A = np.random.randint(0, 10, (N, M))
print(str(A) + "\n")

# Создание дополнительной столбца
a = np.random.randint(0, 10, N)
a = a[: , np.newaxis]
print("Допонлительный столбец: \n" + str(a))

# Добавление столбца под номером K
print("\n K = " + str(K))

if K == M:
    X = np.hstack((A, a))
elif K != M:
    X = np.array(A[:, 0])
    X = X[: , np.newaxis]
    for i in range (1, M):
        if i == K:
            X = np.hstack((X, a))
            Y = A[:, i]
            Y = Y[: , np.newaxis]
            X = np.hstack((X, Y))
        elif i != K:
            Y = A[:, i]
            Y = Y[:, np.newaxis]
            X = np.hstack((X, Y))

print("\nНовая матрица: \n" + str(X))