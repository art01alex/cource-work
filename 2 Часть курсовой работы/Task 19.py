#имя файла: Task 19.py
#номер версии: 1.0
#автор и его учебная группа: Александровский А.П., ЭУ-142
#дата создания: 22.05.2019
#связанные файлы: пакет numpy
#версия Python: 3.6
#ОПИСАНИЕ:  Создать квадратную матрицу A, имеющую N строк и N столбцов со
            #случайными элементами. Определить сумму элементов, расположенных
            #параллельно главной диагонали (ближайшие к главной). Элементы главной
            #диагонали имеют индексы от [0,0] до [N,N].





# Подключение библиотеки Numpy и Random
import numpy as np
import random

# Число строк и столбцов
N = random.randint(2, 10)

# Создание матрицы
A = np.random.randint(0, 10, (N, N))
print(str(A) + "\n")

# Нахождение элементов расположенных параллельно главной диагонали
a = np.diagonal(A, 1)
a_sum = a.sum()
print("Элементы которые выше главной диагонали: \n" + str(a) + "\nИх сумма = " + str(a_sum))

b = np.diagonal(A, -1)
b_sum = b.sum()
print("Элементы которые ниже главной диагонали: \n" + str(b) + "\nИх сумма = " + str(a_sum))