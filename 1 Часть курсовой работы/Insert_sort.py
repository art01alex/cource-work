def insert_sort(arr, dim):
    alg_count = [0, 0]

    for i in range(1, dim):
        top = arr[i]
        j = i - 1
        while j >= 0:
            alg_count[0] += 1
            if arr[j] > top:
                alg_count[1] += 1
                arr[j + 1] = arr[j]
                arr[j] = top
            j -= 1
    return alg_count

#import random
#dim = 40
#arr = [random.randint(0, 100) for i in range(0, dim)]
#print(insert_sort(arr, dim))