# The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

#     If a[i] > b[i], then Alice is awarded 1 point.
#     If a[i] < b[i], then Bob is awarded 1 point.
#     If a[i] = b[i], then neither person receives a point.

# Comparison points is the total points a person earned.

# Given a and b, determine their respective comparison points. 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    points4A = 0
    points4B = 0
    allpoints = 0
    for i,j in zip(a,b):
        # for j in range(len(b)):
            if i > j:
                #   print(f"{a[i]} is greater than {b[j]}")
                points4A += 1
            elif i < j:
                points4B += 1
            elif i == j:
                allpoints += 0 
                
    allpoints = points4A , points4B           
    return allpoints

    

if __name__ == '__main__':
  

    a = [17, 28, 30]

    b = [99, 16, 8]

    result = compareTriplets(a, b)
    print(result)

   
# Example

# a = [1, 2, 3]
# b = [3, 2, 1]

#     For elements *0*, Bob is awarded a point because a[0] .
#     For the equal elements a[1] and b[1], no points are earned.
#     Finally, for elements 2, a[2] > b[2] so Alice receives a point.

# The return array is [1, 1] with Alice's score first and Bob's second.

# Function Description

# Complete the function compareTriplets in the editor below.

# compareTriplets has the following parameter(s):

#     int a[3]: Alice's challenge rating
#     int b[3]: Bob's challenge rating

# Return

#     int[2]: Alice's score is in the first position, and Bob's score is in the second.
   
# # 