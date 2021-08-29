nums = [9, 5, 1, 2, 4, 3, 9]
ln = len(nums)


def counting_sort(nums):
    
    result = [0] * ln
    count_nums = [0] * 100
    for i in range(0, ln):
        count_nums[nums[i]] = count_nums[nums[i]] + 1
    for i in range(1, 10):
        count_nums[i] += count_nums[i - 1]
    i = ln - 1
    while i >= 0:
        result[count_nums[nums[i]] - 1] = nums[i]
        count_nums[nums[i]] = count_nums[nums[i]] - 1
        i = i - 1

    for i in range(0, ln):
        nums[i] = result[i]
    return nums



print('counting sort result:   ', counting_sort(nums))
