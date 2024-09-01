#import necessary module / libraries
import numpy as np

#input list of integers
dimensions_list = [int(d) for d in input().split()]

# print(dimensions_list)

#print a numpy  array containing all 0s with the given dimensions 
print( np.zeros(dimensions_list, dtype = int) )
    
#print a numpy  array containing all 1s with the given dimensions
print( np.ones(dimensions_list, dtype = int) )