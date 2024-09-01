"""
input : 
This program takes dimensions of two 2D arrays , 
value of the dimension for cncatenation, 
and the elements in the two arrays

output :
resultant array after applying concatenation on axis 0
"""


#import necessary modules
import numpy as np

#input 3 integers
n , m , p = map(int, input().split()) 

# print(n,m,p)

array1 = []

# create a 2D array (list of lists) by first taking n list of integers as input and appending them in another list
for i in range(n) :
    #input a list of integers
    tmp_list = [int(x) for x in input().split()]
    
    array1.append(tmp_list)
    
array2 = []

# create a 2D array (list of lists) by first taking m list of integers as input and appending them in another list
for i in range(m) :
    #input a list of integers
    tmp_list = [int(x) for x in input().split()]
    
    array2.append(tmp_list)

# print(array1)
# print(array2)

print(np.concatenate( (array1 , array2),axis=0) )


