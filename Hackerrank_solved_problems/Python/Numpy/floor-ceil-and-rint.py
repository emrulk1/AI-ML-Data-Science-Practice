#import necessary module/libraries
import numpy as np

np.set_printoptions(legacy='1.13')
#used to set numpy print formatting related options 
#https://stackoverflow.com/questions/60011875/what-is-legacy-for-numpy-set-printoptionslegacy-1-13

#takes a list of floating point numbers as input
arr = [float(x) for x in input().split()]

#for each element x in the list, print the nearest integer less than or equal to x 
print(np.floor(arr))

#for each element x in the list, print the nearest integer greater than or equal to x
print(np.ceil(arr))

#for each element x in the list, print the integer closest to x
print(np.rint(arr))



