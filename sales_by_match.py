
#https://www.hackerrank.com/challenges/sock-merchant/problem
import math
import os 
import random
import re
import sys


def sockMerchant(n, ar):
    count = 0
    colors = dict()
    for color in ar:

        if (color in colors):
            count += 1
            del colors[color]
        else:
            colors[color] = 0
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
