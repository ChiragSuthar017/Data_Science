import numpy as np

# Create a 3×3 array filled with random numbers and print its shape.

print("Create a 3×3 array filled with random numbers and print its shape.")

value = [1,3,6,8,9,4,7,2,5]
arr = np.random.choice(value , (3, 3))
print(arr)
print("shape : ", arr.shape)
print("\n")

# Convert an array of floats [1.1, 22, 3.3] into integers.
print("Convert an array of floats [1.1, 2.2, 3.3] into integers.")
a = np.array([1.1, 22, 3.3])
print(a)
print("data type", a.dtype)
b = a.astype('int64')
print(b)
print("data type", b.dtype)
print("\n")

# Use fancy indexing to extract even numbers from [1, 2, 3, 4, 5, 6].
print("Use fancy indexing to extract even numbers from [1, 2, 3, 4, 5, 6].")
ev = np.array([1, 2, 3, 4, 5, 6])
print(ev)
print(ev[ev %2== 0])
print("\n")

# Reshape a 1D array of size 9 into a 3×3 matrix.
print("Reshape a 1D array of size 9 into a 3×3 matrix.")

c = np.array([1,2,3,4,5,6,7,8,9])
print(c)
print("reshape array is : ")
print(c.reshape(3, 3))
print("\n")

# Use boolean masking to filter numbers greater than 50 in an array.
print("Use boolean masking to filter numbers greater than 50 in an array.")

d = np.array([11,22,33,44,55,66,77,88,99,100])
print(d)
print(d[d>50])