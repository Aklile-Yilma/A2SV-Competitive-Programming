#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    nums = [0] * (n+2)
    
    for start, end, num in queries:
        nums[start-1] += num
        nums[end] -= num
    
    #compute prefix
    max_num = 0
    prefix = 0
    for idx in range(len(nums)):
        prefix += nums[idx]
        max_num = max(max_num, prefix)
        
    return max_num
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
        
    fptr.write(str(result) + '\n')

    fptr.close()
