#import necessary modules/libraries
from cgitb import reset
import numpy as np

# take whole line input, split based on space and convert to 2 integers
n , m = map(int, input().split())

matrix = []

#create a 2D array by first input n lists of integers and one by one appending them in a list
for i in range(n) :
    row_list = [int(item) for item in input().split()]
    matrix.append(row_list)

# Compute the sum along axis , then the product of that sum. 
result = np.prod(np.sum(matrix, axis = 0) )

print(result)

