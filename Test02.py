
def remove(nums, n, value):
    index = 0
    for i in range(n):
        if nums[i] != value:
            nums[index] = nums[i]
            index += 1
            
    for i in range(index):
        print(nums[i], end=' ')

nums = [3, 5, 7, 9, 4, 9, 1]
remove(nums, len(nums), 5)