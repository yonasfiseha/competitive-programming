
nums = [3, 5, 2, 1, 7, 8, 4]

def insertion_sort(nums):
    ln = len(nums)
    for i in range(1, ln):
        unsorted_first_value = nums[i]
        element = i
        while unsorted_first_value < nums[element - 1] and element > 0:
            nums[element] = nums[element - 1]
            element -= 1

            nums[element] = unsorted_first_value


insertion_sort(nums)
print(nums)
