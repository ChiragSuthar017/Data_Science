import pandas as pd

print("Series ")
# its give autometic index like 0 1 2 3.....
print("give autometic index")
a = pd.Series([96,72,77,89,76,68])
print(a)
print(type(a))
print("\n")

# we can define the index
print("we can define the index") 
b = pd.Series([96,72,77,89,76,68],["chirag","nathu","chaman","ram","honda","kasri"])
print(b)
print(b["chirag"])
print(b["ram"])
print("\n")

# Data Frame
print("Data frame")

data = {
    "name" : ["Chirag","prince","bhavy"],
    "age"  : [20,21,19],
    "city" : ["rajasthan","gujarat","delhi"]
}
print(data)
c = pd.DataFrame(data)
print(c)

print(c.index)
print(c.columns)