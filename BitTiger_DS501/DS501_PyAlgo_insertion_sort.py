def insertion_sort(arr):
    for i in range(1, len(arr)): # starting from the second element
        key = arr[i]
        j = i - 1 # compare with the all elements in front of key
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j] # move to right hand side
            j -= 1
        arr[j+1] = key # insert the key to the correct place

import random

print('='*20)
arr = random.sample(range(1000), 20)
print('Input:', arr)
insertion_sort(arr)
print('Output:', arr)

print('='*20)
arr = random.sample(range(-1000, 1000), 20)
print('Input:', arr)
insertion_sort(arr)
print('Output:', arr)
