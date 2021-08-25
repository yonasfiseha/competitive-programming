def Bubble_sort(nums):
    ln = len(nums)
    for i in range(0, ln - 1):
        for j in range(0, ln - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


print(Bubble_sort([5, 6, 10, 2, 1, 9, 12, 15]))

