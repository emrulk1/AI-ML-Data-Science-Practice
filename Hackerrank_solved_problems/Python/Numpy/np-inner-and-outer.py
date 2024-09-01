"""
Given 2 1D arrays as input
Thisprogram prints the inner and outer product of the two arrays
"""

#import necessary module/libraries
import numpy as np

#input a list of integers
tmp_list = [int(x) for x in input().split()]

#convert list to numpy array
A = np.array(tmp_list)

#input a list of integers
tmp_list = [int(x) for x in input().split()]

#convert list to numpy array
B = np.array(tmp_list)

print(np.inner(A , B) )
print(np.outer(A , B) )


