"""
This program takes the coefficients of a polynomial  and a point as input and
outputs the value of the polynomial at the given point
"""

#import necessary module / libraries
import numpy as np

# input a list of floating point numbers 
P = [float(x) for x in input().split()]

#take a line as input and convert to a floating point number
x = float(input().strip())


print(np.polyval(P, x) )
