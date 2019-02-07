def merge_sort(arr):
    def merge(arr, head, mid, tail):
        n1 = mid - head + 1 # first array is arr[head, .., mid]
        n2 = tail - mid # second arr is arr[mid+1, ..., tail]

        # create temp arrays
        L = [0] * n1
        R = [0] * n2

        # copy data to temp array L[] and R[]
        for i in range(0, n1):
            L[i] = arr[head+i]
        for j in range(0, n2):
            R[j] = arr[mid+1+j]

        # merge the temp arrays back into arr[head,...,tail]
        i = 0
        j = 0
        k = head

        while i < n1 and j < n2:
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # copy the remaining elements, if there are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def divide(arr, head, tail):
        if head < tail:
            mid = head + (tail - head)//2
            divide(arr, head, mid)
            divide(arr, mid+1, tail)
            merge(arr, head, mid, tail)


    divide(arr, 0, len(arr)-1)

import random

print('='*20)
arr = random.sample(range(1000), 20)
print('Input:', arr)
merge_sort(arr)
print('Output:', arr)

print('='*20)
arr = random.sample(range(-1000, 1000), 20)
print('Input:', arr)
merge_sort(arr)
print('Output:', arr)
