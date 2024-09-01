#import necessary libraries
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    
    # the reverse() method directly modify the list and reverse the contents of the list object in-place 
    # https://www.geeksforgeeks.org/python-reversing-list/
    arr.reverse()
    return numpy.array(arr, float)

#input a list of elements by taking whole line input , split into elements based on space and stroing them in a list
arr = input().strip().split(' ')

#returns the reverse of a list as a numpy float array
result = arrays(arr)

print(result)