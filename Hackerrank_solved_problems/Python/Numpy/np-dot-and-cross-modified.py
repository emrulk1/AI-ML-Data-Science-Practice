#import necessary modules/libraries
import numpy as np

n = int(input())

# print(n)

A = []

#create a 2D array(list of lists) by first input n lists of integers and one by one appending them in a list
for i in range(n) :
    rowList = [int(item) for item in input().split()]
    A.append(rowList)

# convert from list of lists to numpy nd array
A = np.array(A)   
# print(A)

B = []

#create a 2D array(list of lists) by first input n lists of integers and one by one appending them in a list
for i in range(n) :
    rowList = [int(item) for item in input().split()]
    B.append(rowList)

# convert from list of lists to numpy nd array
B = np.array(B)

#computes the matrix multiplication of 2 numpy arrays using dot()
print(np.dot(A,B))
