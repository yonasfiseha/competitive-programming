#https://www.hackerrank.com/challenges/find-the-median/problem

nums = [0, 1, 2, 4, 6, 5, 3]
ln = len(nums)
1<= ln <= 1000001
-10000 <= nums[ln - 1] <= 10000



def Median(nums):
    nums.sort()
    if ln % 2 == 0:
        val = ln // 2
        median_value = nums[val]
    elif ln % 2 != 0:
        val2 = (ln - 1) // 2
        median_value = nums[val2]
    return median_value


print(Median(nums))


