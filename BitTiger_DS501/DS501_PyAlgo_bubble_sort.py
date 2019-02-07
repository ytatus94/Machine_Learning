def bubble_sort(arr):
    for i in range(len(arr)-1): # i cannot reach the last element to aviod j = i + 1 overflow
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

import random

arr = []
bubble_sort(arr)
print(arr)

print('='*20)
arr = random.sample(range(1000), 20)
print('Input:', arr)
bubble_sort(arr)
print('Output:', arr)

print('='*20)
arr = random.sample(range(-1000, 1000), 20)
print('Input:', arr)
bubble_sort(arr)
print('Output:', arr)
