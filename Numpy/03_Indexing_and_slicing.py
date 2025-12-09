import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a)
flat = a.flatten()
print(flat,"\n")

# Index
print("Indexing")
print(flat[0])
print(flat[4])
print(flat[1:5])
print(flat[:6]) # its equal to 0:6
print(flat[3:]) # its equal to 3:end of array index
print(flat[::2]) # give every second elements 
print("\n")

# Slicing
print("slicing")
b = flat[2:6] # Make slice 
print(b)
b[0] = 12 # if we change slice then affect original array
print(b)
print(flat)
c = flat[2:6].copy() # this is not a slice because we are using copy method to get the copy
print(c)
c[0] = 22
print(c)
print(flat,"\n")

# Fancy indexing (select multiple index)
print("Fancy indexing")
d = np.array([1,2,3,4,5,6,7,8,9])
print(d)
print(d[[2,5,7]])
print("\n")

# Boolean masking (filter data)
print("Boolean masking")
e = np.array([1,2,3,4,5,6,7,8,9])
print(e)
print(e[e>5])