import numpy as np 

arr = np.array([1,2,3,4,5])
print(arr)
# vectorized operations 
print("vectorized operations")
result = arr ** 2
print(result)
print("\n")

# broadcasting 
print("broadcasting")
a = np.array([1,2,3,4,5])
print(a)
b = a + 10
print(b)
print("\n")

# Broadcasting with Two Arrays
print("Broadcasting with Two Arrays")
arr1 = np.array([1,2,3])
arr2 = np.array([10,20,30])
re = arr1 + arr2 # element wise additions 
print(re)
print("\n")

# Broadcasting a 2D Array and a 1D Array 
print("Broadcasting a 2D Array and a 1D Array")
arr3 = np.array([[1,2,3],[4,5,6]])
arr4 = np.array([1,2,3])
res = arr3 + arr4  # Broadcasting arr2 across arr1
print(res)
print("\n")

# Normalizing Data Using Broadcasting
print(" Normalizing Data Using Broadcasting")
data = np.array([[10,20,30],
                 [15,25,35],
                 [20,30,40],
                 [25,35,45],
                 [30,40,50]])
# calculating mean and standerd division for each feature (column)
mean = data.mean(axis=0)
std = data.std(axis=0)

# Normalizing the data using broadcasting
normalization = (data - mean) / std 
print(normalization)