import numpy as np

# Create 1D array
print("1D array")
a = np.array([1,2,3,4])
print(a,"\n")

# Create 2D and 3D array
print("2X2 array")
b = np.array([[1,2,3], [4,5,6]])
print(b,"\n")

print("3X3 array")
c = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(c,"\n")

 # Creating arrays from scratch 

print("Creating arrays from scratch \n")

print("3X3 array of zeros ")
print(np.zeros((3, 3)))
print("\n")

print("2X4 array of ones ")
print(np.ones((2, 4)))
print("\n")

print("3X3 array filling with any number like 7")
print(np.full((3, 3),7))
print("\n")

# Make identitiy matrix 

print("Identity matix ")
print(np.eye(4))
print("\n")

# create array using range

print("array using range")
print(np.arange(1 , 20))
print("\n")

# array using range range with addition like
# if np.arange is 1  , 10 ,2 so answer is 1 , 3 , 5 ... 
# for ecample add 2 in 1 or 1+2 is 3 so add 2 in 3+2 etc 
print("array using range with addition ")
print(np.arange(1,20,2))
print("\n")

# Create array on equally spaced of given element 
print("Create array on equally spaced on given element")
print(np.linspace(1, 100 ,5))# 1 to 100 is range and 5 is equally spaced element 
print("\n")

# Cheking array proparties 
print("Checking array proparies")
d = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(d,"\n")

print("shape", d.shape)
print("size", d.size)
print("dimensions", d.ndim)
print("data type", d.dtype)
print("\n")

# Craete array in float data type
print("create array in float data type")
e = np.array([[1.2,2,3], [4,5,6], [7,8,9]], dtype='float')
print(e)
print("data type", e.dtype)
print("\n")

# Chante data type 
print("Change data type")
f = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(f)
print("data type", f.dtype)
g = f.astype('float')
print(g)
print("data type", g.dtype)
print("\n")

# change shape 
print("reshape")
re = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(re.reshape(2,6))
print("shape", re.shape)
print("\n")

# change in 1D

print("change in 1D")
print(re.flatten())