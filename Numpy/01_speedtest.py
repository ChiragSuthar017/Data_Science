import numpy as np
import time

size = 1_000_000

# Using python list

l1 =    list(range(size))
l2 =    list(range(size))
print("using python list")
start = time.time()
add = [x+y for x,y in zip(l1,l2)]
end = time.time()

print(end - start)

print("\n")

# using Numpy

l3 =    np.array(list(range(size)))
l4 =    np.array(list(range(size)))
print("using python list")
start = time.time()
add = l3+l4
end = time.time()

print(end - start)

print("\n")

# make numpy array
print("make numpy array")
a = np.array([1,2,3,4,5])
print(f"{a} \n")

# make 2D numpy array 
print("make 2D numpy array")
b = np.array([[1,2,3,4], [5,6,7,8]])
print(f"{b} \n")

# check type and shape
print("type", type(a))
print("type", type(b))

print("shape", a.shape)
print(f"shape, {b.shape}\n")

# check memory efficiency - python list vs numpy

import sys

lst = list(range(1000))
num_py = np.array(lst)

print("python list size : " , sys.getsizeof(lst),"bytes")
print("Numpy array size : ", num_py.nbytes,"bytes")