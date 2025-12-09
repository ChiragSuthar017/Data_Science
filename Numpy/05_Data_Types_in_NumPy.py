import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr)
print("data type : ",arr.dtype)
arr1 = arr.astype("float64")
print(arr1)
print("data type after change : ", arr1.dtype)
a = np.array([7,8,9,2,3], dtype="int32")
print(a)
print("data type of a: ",a.dtype)
print("\n")

# nbytes 
print("nbytes : ",arr.nbytes)
print("nbytes of a is : ",a.nbytes)
print("\n")

arr_int64 = np.array([1,2,3], dtype=np.int64)
arr_int32 = np.array([1,2,3], dtype=np.int32)
print("nbytes of arr_int64 : ", arr_int64.nbytes) # Output : 24 bytes(3 elements * 8 bytes each)
print("nbytes of arr_int32 : ", arr_int32.nbytes)