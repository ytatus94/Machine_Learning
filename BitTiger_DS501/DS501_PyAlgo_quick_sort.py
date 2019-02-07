def quick_sort(arr):
    def partition(arr, head, tail):
        first = head
        pivot = arr[first] # use first element as pivot
        head = first+1

        while True:
            # look for arr[head] > pivot elements
            while head <= tail and arr[head] <= pivot:
                head = head + 1
            # look for arr[tail] < pivot elements
            while head <= tail and arr[tail] >= pivot:
                tail = tail - 1

            if tail < head:
                break
            else:
                arr[head], arr[tail] = arr[tail], arr[head]

        arr[first], arr[tail] = arr[tail], arr[first]

        return tail # the pivot index

    def divide(arr, head, tail):
        if head < tail:
            split = partition(arr, head, tail) # partition index
            divide(arr, head, split-1)
            divide(arr, split+1, tail)

    divide(arr, 0, len(arr)-1)

import random

arr = []
quick_sort(arr)
print(arr)

print('='*20)
arr = random.sample(range(1000), 20)
print('Input:', arr)
quick_sort(arr)
print('Output:', arr)

print('='*20)
arr = random.sample(range(-1000, 1000), 20)
print('Input:', arr)
quick_sort(arr)
print('Output:', arr)
