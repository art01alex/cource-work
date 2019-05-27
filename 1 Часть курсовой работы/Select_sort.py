def select_sort(arr, dim):
    alg_count = [0, 0]
    for i in range(0, dim):
        min = i
        for j in range(i + 1, dim):
            alg_count[0] += 1
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            alg_count[1] += 1
    return alg_count

import random
dim = 40
arr = [random.randint(0, 100) for i in range(dim)]
print(arr)
print(select_sort(arr, dim))