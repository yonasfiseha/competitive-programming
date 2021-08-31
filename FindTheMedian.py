#https://www.hackerrank.com/challenges/find-the-median/problem
import math
import os
import random
import re
import sys


nums = [0, 1, 2, 4, 6, 5, 3]
ln = len(nums)
1<= ln <= 1000001
-10000 <= nums[ln - 1] <= 10000



def Median(nums):
    nums.sort()
    if ln % 2 == 0:
        val = ln // 2
        midian_value = nums[val]
    elif ln % 2 != 0:
        val2 = (ln - 1) // 2
        midian_value = nums[val2]
    return midian_value


print(Median(nums))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ln = int(input().strip())

    nums = list(map(int, input().rstrip().split()))

    result = Median(nums)

    fptr.write(str(result) + '\n')

    fptr.close()

