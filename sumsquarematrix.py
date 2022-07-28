# Sum of square matrix diagonals.
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix
# is shown below:
# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = 1 + 5 + 9 = 15.
# The right to left diagonal = 3 + 5 + 9 = 17 . Their absolute difference is 17 - 15 = 2.

# Function description
# Complete the diagonalDifference
# function in the editor below.

# diagonalDifference takes the following parameter:

#     int arr[n][m]: an array of integers

# Return

#     int: the absolute diagonal difference

# Input Format

# The first line contains a single integer,n,the number of rows and columns in the square matrix arr.
# Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].
# Output Format
# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.
# Sample Input

# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# Sample Output
# 15

# Explanation
# The primary diagonal is:

# 11
#    5
#      -12

# Sum across the primary diagonal: 11 + 5 - 12 = 4
# The secondary diagonal is:

#      4
#    5
# 10

# Sum across the secondary diagonal: 4 + 5 + 10 = 19
# Difference: |4 - 19| = 15
#My Logical plan 
# 1st diagonal  left - right (0,0),(1,1),(2,2)
# 2nd diagonal  right - left (0,2),(1,1),(2,0)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_right = 0
    right_left = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[0][0]:
                print(arr[i][j])
                left_right += arr[i][j]
            elif arr[i][j] == arr[1][1]:
                print(arr[i][j])
                left_right += arr[i][j]
            elif arr[i][j] == arr[2][2]:
                print(arr[i][j])
                left_right += arr[i][j]
    print(f"Total left-right :- {left_right}")
    print("******************************************")
    for k in range(len(arr)):
        for l in range(len(arr)):
            if arr[k][l] == arr[0][2]:
                print(arr[k][l])
                right_left += arr[k][l]
            elif arr[k][l] == arr[1][1]:
                print(arr[k][l])
                right_left += arr[k][l]
            elif arr[k][l] == arr[2][0]:
                print(arr[k][l])
                right_left += arr[k][l]
    return right_left - left_right


if __name__ == '__main__':
    n = 3
    arr = [[11, 2, 4] ,[4, 5, 6], [10, 8, -12]]
    result = diagonalDifference(arr)
    print(result)

    