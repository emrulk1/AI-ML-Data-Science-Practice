#import necessary modules/libraries
import numpy as np

# take whole line input, split based on space and convert to 2 integers
n, m = map(int, input().split())
# print(n,m)
# print(type(n))

matrix = []

#create a 2D array by first input n lists of integers and one by one appending them in a list
for i in range(n) :
    row_list = [int(item) for item in input().split()]
    matrix.append(row_list)
    
# print(matrix)

#computes arithmatic mean, variance and standard daviation a 2D numpy array on different axes (dimension)
mean_val = np.mean(matrix, axis = 1)
variance = np.var(matrix, axis = 0)
std_val = np.std(matrix, axis = None)

print(mean_val)
print(variance)

#prints standard daviation rounded to 11 places after decimal
print(round(std_val,11) )

