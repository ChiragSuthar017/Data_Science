import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr, "\n")

# Axis 
print("Axis")
print(arr[0]) 
print(arr[1]) 

# sum of axis
print("axis 0 is rows")
print("axis 1 is columns")
print("axis 2 is depth \n")
print("sum of axes")
print("sum rows")
rows = np.sum(arr , axis=0)
print(rows)
print("\n")

print("sum of columns")
columns = np.sum(arr , axis=1)
print(columns)
print("\n")

# indexing 
print("Indexing")
print(arr[0])
print(arr[0][1])
print(arr[0:2 , 1:3])
print("\n")

arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
print(arr3d[0,1,2])
print(arr3d[:,0,: ])