def selection_sort(nums):

    ln = len(nums)
    for i in range(0, ln-1):
        min_value = i
        for j in range(i + 1, ln):
            if nums[j] < nums[min_value]:
                min_value = j
        
        nums[i], nums[min_value] = nums[min_value], nums[i]
    


nums = [6, 2, 9, 12, 5, 1, 3]
selection_sort(nums)
print(nums)