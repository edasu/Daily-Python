
#1

import numpy as np

#2

array1 = np.arange(15,41) #this array is contains 40
array2 = np.arange(10,25) #thisis not contains 25, because its until 25

array1

array2

#3

even_aaray1 = np.arange(2,21,2)
even_1 = even_aaray1[0:5]
even_2 = even_aaray1[5:]

even_aaray2 = np.arange(34,43,2)
even_aaray2

arrays = even_aaray2, even_aaray1
arrays

np.matrix(np.stack((even_1, even_2, even_aaray2)))

#4

matrix = np.arange(36).reshape(6,6)
matrix

m = np.random.randn(5,2)
m

m[4,1]



#5

mt = matrix.copy()
mt

mt.min()

mt.max()

mt.mean()

mt.std()

mt.var()

