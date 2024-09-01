import numpy as np


#take whole line input, split based on space and conver to 2 integers
n, m = map(int, input().split())
# print(n,m)
# print(type(n))

matrix = []

#create a 2D array by input n lists of integers and one by one appending the n lists in a list 
for i in range(n) :
    #input a list of integers
    row_list = [int(item) for item in input().split()]
    
    matrix.append(row_list)
    
# print(matrix)

#perform the min function over axis 1 of @D numpy array and then find the max of that.
result = np.max(np.min(matrix, axis = 1) )

print(result)

