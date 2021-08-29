#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(nums):
    ln = len(nums)
    result = [0] * ln
    count = [0] * 100

    for i in range(0, ln):
        count[nums[i]] = count[nums[i]] + 1
    for i in range(1, 100):
        count[i] += count[i - 1]
    i = ln - 1
    while i >= 0:
        result[count[nums[i]] - 1] = nums[i]
        count[nums[i]] -= 1
        i = i - 1

    for i in range(0, ln):
        nums[i] = result[i]
    return nums



    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums = int(input().strip())

    nums = list(map(int, input().rstrip().split()))

    result = countingSort(nums)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
