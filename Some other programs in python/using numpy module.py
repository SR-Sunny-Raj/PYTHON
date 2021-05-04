from numpy import linspace, concatenate
nums = [25, 36, 95, 14, 12, 26]
nums2 = [1, 2, 3, 4, 5]
print(nums)
del nums[2:5]
print(nums)

x = linspace(0, 4, 30)
print(x)

arr = concatenate([nums, nums2])
print(arr)
