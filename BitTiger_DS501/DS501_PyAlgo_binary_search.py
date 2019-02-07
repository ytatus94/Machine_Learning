class Solution():
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

s = Solution()

import random
arr = random.sample(range(1000), 20)
tar = arr[0]
arr = sorted(arr)

print('Input :', arr)
print('Target:', tar)
idx = s.search(arr, tar)
print('Output:', idx)

print('=' * 20)

arr = random.sample(range(-1000, 1000), 20)
tar = arr[0]
arr = sorted(arr)

print('Input :', arr)
print('Target:', tar)
idx = s.search(arr, tar)
print('Output:', idx)
