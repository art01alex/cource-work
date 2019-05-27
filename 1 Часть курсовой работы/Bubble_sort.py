def bubble_sort(arr, dim):
    alg_count = [0, 0]
    for j in range(0, dim-1):
        for i in range(0, dim-1):
            alg_count[0] += 1
            if arr[i] > arr[i + 1]:
                alg_count[1] += 1
                arr[i] , arr[i + 1] = arr[i + 1] , arr[i]
    return alg_count


#import random
#dim = 40
#arr = [random.randint(0, 100) for i in range(dim)]
#print(bubble_sort(arr, dim))