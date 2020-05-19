input_array = [0, 0, 1]


def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    append_at = 0
    for i in range(0, len(nums)):
        if nums[i] != 0:
            nums[append_at] = nums[i]
            nums[i] = 0
            append_at += 1


moveZeroes(input_array)
print(input_array)
