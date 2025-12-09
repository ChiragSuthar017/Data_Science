import numpy as np

arr = np.array([1,2,3,3,4,5])
print(arr)
arr1 = ([1,2,3,4,5])
arr2 = ([6,7,8,9,10])

# np.mean() – Compute the mean (average) of an array.
print("mean : ", np.mean(arr))

# np.std() – Compute the standard deviation of an array.
print("std : ", np.std(arr))

# np.var() – Compute the variance of an array.
print("variance : ",np.var(arr) )

# np.min() – Compute the minimum value of an array.
print("minimum : ", np.min(arr))

# np.max() – Compute the maximum value of an array.
print("maximum : ", np.max(arr))

# np.sum() – Compute the sum of all elements in an array.
print("sum : ", np.sum(arr))

# np.prod() – Compute the product of all elements in an array.
print("product : ", np.prod(arr))

# np.median() – Compute the median of an array.
print("median : ", np.median(arr))

# np.percentile() – Compute the percentile of an array.
print("percentile : ", np.percentile(arr , 50))

# np.argmin() – Return the index of the minimum value in an array.
print("return the index of minimum value : ", np.argmin(arr))

# np.argmax() – Return the index of the maximum value in an array.
print("return the index of maximum value : ", np.argmax(arr))

# np.corrcoef() – Compute the correlation coefficient matrix of two arrays.
print("corrcoef : ",np.corrcoef(arr1 , arr2))

# np.unique() – Find the unique elements of an array.
print("unique : ", np.unique(arr))

# np.diff() – Compute the n-th differences of an array.
print("difference : ",np.diff(arr))

# np.cumsum() – Compute the cumulative sum of an array.
print("cumulative sum : ", np.cumsum(arr))

# np.linspace() – Create an array with evenly spaced numbers over a specified interval.
print("linespace : ", np.linspace(0 , 10 ,5))

# np.log() – Compute the natural logarithm of an array.
print("log : ", np.log(arr))

# np.exp() – Compute the exponential of an array.
print("exponential of an array : ", np.exp(arr))