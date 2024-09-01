#import necessary modules/libraries
import numpy as np

# take whole line input, split based on space and convert to 2 integers
n, m = map(int, input().split())

M = []

#create a 2D array by first input n lists of integers and one by one appending them in a list
for i in range(n) :
    rowList = [int(item) for item in input().split()] 
    M.append(rowList)

# print(M)
# print(type(M))
# M = np.transpose(M)

#convert from list of lists to numpy nd array
M = np.array(M)
# print(type(M))

print(np.transpose(M))

#flatten creates a copy of the input array flattened to one dimension.
print(M.flatten())
