"""
This program takes dimension of a 2D array as input and
output a 2D array of dimension nXm with 1's in the main diagonal and 0's elsewhere
"""

#import nexessary library / modules
import numpy as np

np.set_printoptions(legacy='1.13')
#used to set numpy print formatting related options 
#https://stackoverflow.com/questions/60011875/what-is-legacy-for-numpy-set-printoptionslegacy-1-13

#take 2 ingegers as input
n, m = map(int, input().split())

#print a 2-D array with 1's in the main diagonal and 0's elsewhere
print( np.eye(n , m, k = 0) )