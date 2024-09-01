#import necessary modules/libraries
import numpy as np

# take whole line input, split based on space and convert to 2 integers
n , m = map(int, input().split())

# print(n,m)

A = []
#create a 2D array(list of lists) by first input n lists of integers and one by one appending them in a list

for i in range(n) :
    rowList = [int(x) for x in input().split()]
    A.append(rowList)

# print(A)

A = np.array(A)

# print(A + A)

B = []

#create a 2D array(list of lists) by first input n lists of integers and one by one appending them in a list

for i in range(n) :
    rowList = [int(x) for x in input().split()]
    B.append(rowList)

#print different arithmatic operations on numpy 2d array using operators (operator overload)    
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)

