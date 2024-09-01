import numpy as np

#take the whole line as input , split them based on spce , convert each of them into integers and store them in list 
arr_1d = list(map(int, input().split())) 

#make a 2d array of dimension 3X3 from list
arr_2d = np.reshape(arr_1d, (3,3))


print(arr_2d)
