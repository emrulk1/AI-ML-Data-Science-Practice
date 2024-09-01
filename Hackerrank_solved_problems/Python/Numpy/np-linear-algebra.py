import numpy as np

n = int(input())

A = []
#create a 2D array(list of lists) by first input n lists of floats and one by one appending them in a list
for i in range(n) :
    rowList = [float(x) for x in input().split()]
    A.append(rowList)

#convert list of lists to numpy n dimensional array
A = np.array(A)

#print the value of determinant of numpy array A rounded 2 decimal points
print(round(np.linalg.det(A), 2) )
